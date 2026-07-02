from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import BaseModel

class CalendarEvent(BaseModel):
    __tablename__ = 'calendar_events'
    
    email_id = Column(String, ForeignKey('emails.id', ondelete='SET NULL'), nullable=True)
    google_event_id = Column(String, nullable=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default="created")
    
    email = relationship("Email", back_populates="calendar_events")
