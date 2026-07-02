from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.review_queue import ReviewQueue
from app.models.email import Email
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/review", tags=["Review Queue"])

class ReviewItem(BaseModel):
    id: str
    email_id: str
    status: str
    suggested_action: str
    confidence: int
    reason: str
    email_subject: str
    email_sender: str
    
    class Config:
        from_attributes = True

@router.get("/", response_model=List[ReviewItem])
def list_review_queue(user_id: str, db: Session = Depends(get_db)):
    items = db.query(ReviewQueue).join(Email).filter(
        Email.user_id == user_id,
        ReviewQueue.status == "PENDING"
    ).all()
    
    return [
        {
            "id": item.id,
            "email_id": item.email_id,
            "status": item.status,
            "suggested_action": item.suggested_action,
            "confidence": item.confidence,
            "reason": item.reason,
            "email_subject": item.email.subject,
            "email_sender": item.email.sender_name
        }
        for item in items
    ]

@router.post("/{item_id}/approve")
def approve_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(ReviewQueue).filter(ReviewQueue.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404)
        
    item.status = "APPROVED"
    item.email.status = "APPROVED_MANUAL"
    item.email.classification = item.suggested_action
    
    db.commit()
    return {"status": "approved"}

@router.post("/{item_id}/reject")
def reject_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(ReviewQueue).filter(ReviewQueue.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404)
        
    item.status = "REJECTED"
    item.email.status = "REJECTED"
    
    db.commit()
    return {"status": "rejected"}
