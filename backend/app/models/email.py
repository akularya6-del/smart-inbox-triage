from sqlalchemy import Column, String, ForeignKey, JSON, DateTime, Integer
from sqlalchemy.orm import relationship
from app.database import BaseModel

class Email(BaseModel):
    __tablename__ = 'emails'
    
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    gmail_message_id = Column(String, index=True, nullable=False)
    thread_id = Column(String, index=True, nullable=False)
    subject = Column(String, nullable=True)
    sender_name = Column(String, nullable=True)
    sender_email = Column(String, index=True, nullable=True)
    snippet = Column(String, nullable=True)
    body_text = Column(String, nullable=True)
    body_html = Column(String, nullable=True)
    labels = Column(JSON, default=list)
    internal_date = Column(String, nullable=True) # Unix timestamp string from Gmail
    received_at = Column(DateTime, nullable=True)
    processed_at = Column(DateTime, nullable=True)
    classification = Column(String, nullable=True)
    confidence = Column(Integer, nullable=True)
    status = Column(String, nullable=True)
    hash = Column(String, unique=True, index=True, nullable=False)
    
    user = relationship("User", back_populates="emails")
    classifications_history = relationship("Classification", back_populates="email", cascade="all, delete-orphan")
    review_items = relationship("ReviewQueue", back_populates="email", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="email", cascade="all, delete-orphan")
    calendar_events = relationship("CalendarEvent", back_populates="email", cascade="all, delete-orphan")
