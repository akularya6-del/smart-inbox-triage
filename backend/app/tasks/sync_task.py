from sqlalchemy.orm import Session
from datetime import datetime, timezone
import structlog

from app.models.user import User
from app.models.oauth_token import OAuthToken
from app.models.setting import Setting
from app.models.email import Email
from app.models.job_log import JobLog
from app.models.job import Job
from app.config import settings
from app.core.security import decrypt_token
from app.services.gmail_service import GmailService
from app.services.email_normalizer import normalize_email
from sqlalchemy.exc import IntegrityError

logger = structlog.get_logger(__name__)

def sync_user_emails(user_id: str, db: Session, job_id: str = None) -> dict:
    """Sync emails for a given user"""
    start_time = datetime.now(timezone.utc)
    items_processed = 0
    errors = 0
    
    token = db.query(OAuthToken).filter(OAuthToken.user_id == user_id).first()
    if not token:
        logger.error(f"No OAuth token for user {user_id}")
        return {"status": "failed", "reason": "No OAuth token"}

    user_settings = db.query(Setting).filter(Setting.user_id == user_id).first()
    max_emails = int(user_settings.max_emails_per_sync) if user_settings else settings.SYNC_MAX_EMAILS
    
    try:
        access_token = decrypt_token(token.access_token)
        refresh_token = decrypt_token(token.refresh_token) if token.refresh_token else None
        
        gmail = GmailService(
            access_token=access_token,
            refresh_token=refresh_token,
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET
        )
        
        # We fetch only UNREAD for triage MVP
        messages_resp = gmail.get_messages_list(max_results=max_emails, query="is:unread")
        messages = messages_resp.get('messages', [])
        
        for msg_ref in messages:
            try:
                # Check if we already have it
                exists = db.query(Email).filter(Email.gmail_message_id == msg_ref['id']).first()
                if exists:
                    continue
                    
                raw_msg = gmail.get_message(msg_ref['id'])
                email_obj = normalize_email(raw_msg, user_id)
                
                db.add(email_obj)
                db.commit()
                items_processed += 1
                
                # Kick off classification inline (or enqueue)
                # We'll do it later in the job or a separate task
                
            except IntegrityError:
                db.rollback()
                logger.warning(f"Email {msg_ref['id']} already exists (IntegrityError).")
            except Exception as e:
                db.rollback()
                logger.error(f"Error processing email {msg_ref['id']}: {str(e)}")
                errors += 1
                
    except Exception as e:
        logger.error(f"Sync failed for user {user_id}: {str(e)}")
        errors += 1
        
    end_time = datetime.now(timezone.utc)
    
    # Log the job if triggered by scheduler
    if job_id:
        log = JobLog(
            job_id=job_id,
            status="COMPLETED" if errors == 0 else "PARTIAL_SUCCESS",
            start_time=start_time,
            end_time=end_time,
            items_processed=items_processed,
            errors=errors
        )
        db.add(log)
        db.commit()

    return {
        "status": "success",
        "processed": items_processed,
        "errors": errors,
        "duration_seconds": (end_time - start_time).total_seconds()
    }
