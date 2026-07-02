from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import BaseModel

class Task(BaseModel):
    __tablename__ = 'tasks'
    
    email_id = Column(String, ForeignKey('emails.id', ondelete='SET NULL'), nullable=True)
    notion_page_id = Column(String, nullable=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(String, nullable=True)
    status = Column(String, default="created")
    
    email = relationship("Email", back_populates="tasks")
