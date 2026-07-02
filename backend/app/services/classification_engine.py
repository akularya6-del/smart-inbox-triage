from sqlalchemy.orm import Session
from app.models.email import Email
from app.models.rule import Rule
from app.models.classification import Classification
from app.services.rule_engine import find_matching_rule

# A simple heuristic-based fallback if no rules match
def heuristic_classify(email: Email) -> dict:
    subject = (email.subject or "").lower()
    body = (email.body_text or "").lower()
    
    if any(word in subject for word in ["invoice", "receipt", "payment"]):
        return {"category": "Finance", "confidence": 75}
    if any(word in subject for word in ["urgent", "action required", "asap"]):
        return {"category": "Urgent", "confidence": 80}
    if "newsletter" in subject or "unsubscribe" in body:
        return {"category": "Newsletter", "confidence": 90}
        
    return {"category": "Uncategorized", "confidence": 50}

def classify_email(email: Email, db: Session) -> dict:
    """Classifies email using rules, then heuristics."""
    rules = db.query(Rule).filter(Rule.user_id == email.user_id, Rule.enabled == True).all()
    
    match = find_matching_rule(email, rules)
    if match:
        return {
            "category": match.action,
            "confidence": 100,
            "rule_id": match.id,
            "reason": f"Matched rule: {match.name}"
        }
        
    return heuristic_classify(email)
