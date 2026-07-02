from sqlalchemy.orm import Session
from app.models.email import Email
from app.models.task import Task
from app.models.calendar_event import CalendarEvent
from app.services.notion_service import create_notion_task
from app.services.calendar_service import create_calendar_event
from app.services.gmail_service import GmailService
from app.services.retry_service import enqueue_retry
from app.core.exceptions import ActionExecutionError
import structlog
import asyncio

logger = structlog.get_logger(__name__)

async def execute_action_for_email(email: Email, db: Session, gmail_service: GmailService):
    """Routes the email to the appropriate action based on its classification"""
    
    category = email.classification or "Uncategorized"
    
    try:
        if category == "Action Required":
            # Create a Notion task
            title = f"Action: {email.subject}"
            desc = f"From: {email.sender_name}\n\n{email.snippet}"
            
            notion_id = await create_notion_task(title, desc)
            
            task = Task(email_id=email.id, notion_page_id=notion_id, title=title, status="created")
            db.add(task)
            
            # Archive in Gmail
            gmail_service.mark_as_read(email.gmail_message_id)
            
        elif category == "Urgent":
            # Priority task + Calendar event
            title = f"URGENT: {email.subject}"
            desc = f"From: {email.sender_name}\n\n{email.snippet}"
            
            notion_id = await create_notion_task(title, desc, priority="High")
            task = Task(email_id=email.id, notion_page_id=notion_id, title=title, priority="High")
            db.add(task)
            
            cal_id = create_calendar_event(f"Review Urgent Email: {email.subject}", desc, gmail_service)
            cal_event = CalendarEvent(email_id=email.id, google_event_id=cal_id, title=title, start_time=None, end_time=None) # timestamps simplified for MVP
            db.add(cal_event)
            
            gmail_service.mark_as_read(email.gmail_message_id)
            
        else:
            # Default action: Just mark as read
            gmail_service.mark_as_read(email.gmail_message_id)
            
        email.status = "COMPLETED"
        logger.info(f"Successfully executed actions for email {email.id} (Category: {category})")
        db.commit()
        
    except ActionExecutionError as e:
        logger.error(f"Action failed for email {email.id}: {str(e)}")
        email.status = "ACTION_FAILED"
        db.commit()
        
        # Enqueue for retry
        enqueue_retry(db, action_type="execute_email_action", params={"email_id": email.id}, error_msg=str(e))
    except Exception as e:
        logger.error(f"Unexpected error executing action for {email.id}: {str(e)}")
        email.status = "ACTION_FAILED"
        db.commit()
