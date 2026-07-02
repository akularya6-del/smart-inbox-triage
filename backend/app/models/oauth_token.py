from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import BaseModel

class OAuthToken(BaseModel):
    __tablename__ = 'oauth_tokens'
    
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    provider = Column(String, default="google")
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True) # encrypted
    expires_at = Column(DateTime, nullable=False)
    
    user = relationship("User", back_populates="oauth_tokens")
