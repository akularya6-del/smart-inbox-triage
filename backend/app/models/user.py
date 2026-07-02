from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.database import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    
    oauth_tokens = relationship("OAuthToken", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("Setting", back_populates="user", uselist=False, cascade="all, delete-orphan")
    emails = relationship("Email", back_populates="user", cascade="all, delete-orphan")
    rules = relationship("Rule", back_populates="user", cascade="all, delete-orphan")
