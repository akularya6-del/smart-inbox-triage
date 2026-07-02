from sqlalchemy.orm import Session
from app.models.email import Email
from app.models.classification import Classification
from app.services.classification_engine import classify_email
from app.services.review_service import evaluate_for_review
import structlog

logger = structlog.get_logger(__name__)

def process_unclassified_emails(db: Session):
    """Fetches all emails with status FETCHED and classifies them."""
    emails = db.query(Email).filter(Email.status == "FETCHED").limit(100).all()
    
    processed = 0
    for email in emails:
        try:
            result = classify_email(email, db)
            
            # Save classification history
            clf = Classification(
                email_id=email.id,
                category=result["category"],
                confidence=result["confidence"],
                reason=result.get("reason"),
                rule_matched=result.get("rule_id")
            )
            db.add(clf)
            
            email.classification = result["category"]
            email.confidence = result["confidence"]
            
            # Decide next step (Review or Auto-Approve)
            evaluate_for_review(email, result, db)
            
            processed += 1
        except Exception as e:
            logger.error(f"Failed to classify email {email.id}: {str(e)}")
            db.rollback()
            
    return processed
