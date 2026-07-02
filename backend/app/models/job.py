from sqlalchemy import Column, String, Integer, DateTime, JSON
from app.database import BaseModel

class Job(BaseModel):
    __tablename__ = 'jobs'
    
    job_type = Column(String, nullable=False) # sync, classify, action, retry
    status = Column(String, nullable=False) # IDLE, RUNNING, RETRYING, FAILED, PAUSED, COMPLETED
    last_run_at = Column(DateTime, nullable=True)
    next_run_at = Column(DateTime, nullable=True)
    items_processed = Column(Integer, default=0)
    error_count = Column(Integer, default=0)
    config = Column(JSON, nullable=True)
