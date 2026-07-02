from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class EmailLabel(BaseModel):
    __tablename__ = 'email_labels'
    
    email_id = Column(String, ForeignKey('emails.id', ondelete='CASCADE'), nullable=False)
    label_name = Column(String, nullable=False)
    
    email = relationship("Email")
