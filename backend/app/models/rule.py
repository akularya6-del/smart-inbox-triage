from sqlalchemy import Column, String, Boolean, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseModel

class Rule(BaseModel):
    __tablename__ = 'rules'
    
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    priority = Column(Integer, default=1)
    conditions = Column(JSON, nullable=False) # Store AND/OR conditions
    action = Column(String, nullable=False) # Category to assign
    created_by = Column(String, default="manual") # manual or learned
    
    user = relationship("User", back_populates="rules")
