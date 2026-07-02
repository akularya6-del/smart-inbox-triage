from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.job import Job
from app.models.job_log import JobLog
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/jobs", tags=["Jobs"])

class JobLogResponse(BaseModel):
    id: str
    status: str
    start_time: datetime
    end_time: Optional[datetime]
    items_processed: int
    errors: int
    
    class Config:
        from_attributes = True

class JobResponse(BaseModel):
    id: str
    name: str
    status: str
    last_run_at: Optional[datetime]
    next_run_at: Optional[datetime]
    logs: List[JobLogResponse]
    
    class Config:
        from_attributes = True

@router.get("/", response_model=List[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    # Limit to 50 for MVP
    jobs = db.query(Job).order_by(Job.created_at.desc()).limit(50).all()
    return jobs
