from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.tasks.sync_task import sync_user_emails
from app.models.email import Email
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/emails", tags=["Emails"])

class EmailResponse(BaseModel):
    id: str
    subject: str
    sender_name: str
    sender_email: str
    snippet: str
    status: str
    classification: Optional[str]

    class Config:
        from_attributes = True

@router.post("/sync")
def trigger_sync(user_id: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Manually trigger an email sync for the user"""
    # In production, do this in background. For MVP, we can run it synchronously 
    # to return results immediately, or run in background. Let's do sync for immediate feedback.
    result = sync_user_emails(user_id, db)
    return result

@router.get("/", response_model=List[EmailResponse])
def get_emails(user_id: str, skip: int = 0, limit: int = 50, status: Optional[str] = None, db: Session = Depends(get_db)):
    """List emails for the user"""
    query = db.query(Email).filter(Email.user_id == user_id)
    if status:
        query = query.filter(Email.status == status)
        
    emails = query.order_by(Email.received_at.desc()).offset(skip).limit(limit).all()
    return emails

@router.get("/{email_id}")
def get_email(email_id: str, db: Session = Depends(get_db)):
    email = db.query(Email).filter(Email.id == email_id).first()
    if not email:
        raise HTTPException(status_code=404, detail="Email not found")
    return email
