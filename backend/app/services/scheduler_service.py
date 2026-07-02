from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.database import SessionLocal
from app.tasks.sync_task import sync_user_emails
from app.tasks.classify_task import process_unclassified_emails
from app.tasks.action_task import process_approved_emails
from app.models.user import User
from app.models.job import Job
from datetime import datetime, timezone
import structlog
import asyncio

logger = structlog.get_logger(__name__)

scheduler = AsyncIOScheduler()

async def run_sync_for_all_users():
    logger.info("Running scheduled sync for all users")
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            # For MVP, just track one job globally or per user
            # Let's create a Job record for the sync
            job = Job(name=f"Sync_{user.id}", status="RUNNING")
            db.add(job)
            db.commit()
            
            # Since sync is synchronous for now, we'll wrap it
            try:
                # We could run this in a threadpool
                await asyncio.to_thread(sync_user_emails, user.id, db, job.id)
                job.status = "COMPLETED"
                job.next_run_at = datetime.now(timezone.utc)
            except Exception as e:
                logger.error(f"Scheduled sync failed for {user.id}: {str(e)}")
                job.status = "FAILED"
            finally:
                db.commit()
    finally:
        db.close()

async def run_classification_and_actions():
    logger.info("Running scheduled classification and actions")
    db = SessionLocal()
    try:
        # 1. Classify unclassified
        await asyncio.to_thread(process_unclassified_emails, db)
        
        # 2. Execute actions for APPROVED
        await process_approved_emails(db)
    except Exception as e:
        logger.error(f"Classification/Action job failed: {str(e)}")
    finally:
        db.close()

def start_scheduler():
    if not scheduler.running:
        # Sync every 5 minutes
        scheduler.add_job(
            run_sync_for_all_users,
            trigger=IntervalTrigger(minutes=5),
            id='sync_job',
            name='Sync Emails',
            replace_existing=True
        )
        
        # Classify and Action every 1 minute
        scheduler.add_job(
            run_classification_and_actions,
            trigger=IntervalTrigger(minutes=1),
            id='process_job',
            name='Process Emails',
            replace_existing=True
        )
        
        scheduler.start()
        logger.info("Scheduler started successfully")
