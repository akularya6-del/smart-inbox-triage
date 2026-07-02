from sqlalchemy.orm import Session
from app.models.email import Email
from app.models.review_queue import ReviewQueue
import structlog

logger = structlog.get_logger(__name__)

def evaluate_for_review(email: Email, classification_result: dict, db: Session):
    """
    Decides if an email needs manual review before taking action.
    Creates a ReviewQueue item if so, otherwise proceeds to Action Execution.
    """
    confidence = classification_result.get("confidence", 0)
    category = classification_result.get("category", "Uncategorized")
    
    # Thresholds could be configured in Settings, hardcoded for MVP
    NEEDS_REVIEW_THRESHOLD = 85
    HIGH_RISK_CATEGORIES = ["Finance", "Urgent", "Action Required"]
    
    needs_review = False
    reason = ""
    
    if confidence < NEEDS_REVIEW_THRESHOLD:
        needs_review = True
        reason = f"Low confidence ({confidence}%)"
    elif category in HIGH_RISK_CATEGORIES:
        needs_review = True
        reason = f"High risk category ({category})"
        
    if needs_review:
        item = ReviewQueue(
            email_id=email.id,
            status="PENDING",
            suggested_action=category,
            confidence=confidence,
            reason=reason
        )
        db.add(item)
        email.status = "NEEDS_REVIEW"
        logger.info(f"Email {email.id} placed in review queue: {reason}")
    else:
        email.status = "APPROVED_AUTO"
        logger.info(f"Email {email.id} auto-approved for action: {category}")
        
    db.commit()
