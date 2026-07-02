from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import BaseModel

class ReviewQueue(BaseModel):
    __tablename__ = 'review_queue'
    
    email_id = Column(String, ForeignKey('emails.id', ondelete='CASCADE'), nullable=False)
    status = Column(String, default="PENDING") # PENDING, APPROVED, REJECTED, EDITED, EXPIRED
    suggested_action = Column(String, nullable=True)
    action_params = Column(JSON, nullable=True)
    confidence = Column(Integer, nullable=True)
    reason = Column(String, nullable=True)
    
    email = relationship("Email", back_populates="review_items")
