from app.database import BaseModel
from app.models.user import User
from app.models.oauth_token import OAuthToken
from app.models.email import Email
from app.models.email_label import EmailLabel
from app.models.rule import Rule
from app.models.classification import Classification
from app.models.review_queue import ReviewQueue
from app.models.task import Task
from app.models.calendar_event import CalendarEvent
from app.models.job import Job
from app.models.job_log import JobLog
from app.models.retry_queue import RetryQueue
from app.models.audit_log import AuditLog
from app.models.setting import Setting

# Expose models for Alembic and relations
__all__ = [
    "BaseModel", "User", "OAuthToken", "Email", "EmailLabel", "Rule", 
    "Classification", "ReviewQueue", "Task", "CalendarEvent", 
    "Job", "JobLog", "RetryQueue", "AuditLog", "Setting"
]
