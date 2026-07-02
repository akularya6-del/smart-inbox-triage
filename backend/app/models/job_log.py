from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from app.database import BaseModel

class JobLog(BaseModel):
    __tablename__ = 'job_logs'
    
    job_id = Column(String, ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False)
    status = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    items_processed = Column(Integer, default=0)
    errors = Column(Integer, default=0)
    details = Column(String, nullable=True)
