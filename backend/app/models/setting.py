from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import BaseModel

class Setting(BaseModel):
    __tablename__ = 'settings'
    
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    sync_interval_minutes = Column(String, default="5")
    max_emails_per_sync = Column(String, default="50")
    desktop_notifications_enabled = Column(String, default="false")
    theme = Column(String, default="system")
    last_history_id = Column(String, nullable=True)
    config_json = Column(JSON, nullable=True)
    
    user = relationship("User", back_populates="settings")
