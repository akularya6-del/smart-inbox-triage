from sqlalchemy import Column, String, Integer, DateTime, JSON
from app.database import BaseModel

class RetryQueue(BaseModel):
    __tablename__ = 'retry_queue'
    
    action_type = Column(String, nullable=False)
    action_params = Column(JSON, nullable=False)
    attempts = Column(Integer, default=0)
    max_attempts = Column(Integer, default=6)
    next_retry_at = Column(DateTime, nullable=False)
    last_error = Column(String, nullable=True)
    status = Column(String, default="PENDING") # PENDING, COMPLETED, FAILED
