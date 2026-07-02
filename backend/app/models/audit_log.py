from sqlalchemy import Column, String, JSON, DateTime
from app.database import BaseModel

class AuditLog(BaseModel):
    __tablename__ = 'audit_logs'
    
    entity_type = Column(String, nullable=False) # email, review_item, task, job
    entity_id = Column(String, nullable=False)
    old_status = Column(String, nullable=True)
    new_status = Column(String, nullable=True)
    actor = Column(String, nullable=False) # system, user, scheduler
    reason = Column(String, nullable=True)
    metadata_json = Column(JSON, nullable=True)
