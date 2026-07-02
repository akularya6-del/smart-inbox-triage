from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class Classification(BaseModel):
    __tablename__ = 'classifications'
    
    email_id = Column(String, ForeignKey('emails.id', ondelete='CASCADE'), nullable=False)
    category = Column(String, nullable=False)
    confidence = Column(Integer, nullable=False)
    reason = Column(String, nullable=True)
    rule_matched = Column(String, ForeignKey('rules.id', ondelete='SET NULL'), nullable=True)
    
    email = relationship("Email", back_populates="classifications_history")
    rule = relationship("Rule")
