from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta
from app.models.retry_queue import RetryQueue
from app.config import settings
import structlog
import json

logger = structlog.get_logger(__name__)

def enqueue_retry(db: Session, action_type: str, params: dict, error_msg: str):
    item = db.query(RetryQueue).filter(
        RetryQueue.action_type == action_type,
        RetryQueue.status == "PENDING"
    ).first() # Real logic should check params equality, using simple approach for MVP
    
    if item:
        if item.attempts >= item.max_attempts:
            item.status = "FAILED"
            logger.error(f"Retry max attempts reached for {action_type}")
            db.commit()
            return
        item.attempts += 1
    else:
        item = RetryQueue(
            action_type=action_type,
            action_params=params,
            attempts=1,
            max_attempts=settings.RETRY_ATTEMPTS
        )
        db.add(item)
        
    delay = settings.RETRY_DELAYS[min(item.attempts - 1, len(settings.RETRY_DELAYS) - 1)]
    item.next_retry_at = datetime.now(timezone.utc) + timedelta(minutes=delay)
    item.last_error = error_msg
    
    db.commit()
    logger.info(f"Enqueued retry for {action_type}, attempt {item.attempts}, wait {delay}m")
