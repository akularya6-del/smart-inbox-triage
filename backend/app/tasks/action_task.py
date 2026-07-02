from sqlalchemy.orm import Session
from app.models.email import Email
from app.models.oauth_token import OAuthToken
from app.services.action_executor import execute_action_for_email
from app.services.gmail_service import GmailService
from app.core.security import decrypt_token
from app.config import settings
import structlog
import asyncio

logger = structlog.get_logger(__name__)

async def process_approved_emails(db: Session):
    """Finds emails that are APPROVED_AUTO or APPROVED_MANUAL and executes actions."""
    emails = db.query(Email).filter(Email.status.in_(["APPROVED_AUTO", "APPROVED_MANUAL"])).limit(50).all()
    
    if not emails:
        return 0
        
    # We group by user to optimize GmailService instantiation
    users_emails = {}
    for e in emails:
        users_emails.setdefault(e.user_id, []).append(e)
        
    processed = 0
    for user_id, user_emails in users_emails.items():
        token = db.query(OAuthToken).filter(OAuthToken.user_id == user_id).first()
        if not token:
            logger.error(f"No token for user {user_id}, skipping actions.")
            continue
            
        gmail_service = GmailService(
            access_token=decrypt_token(token.access_token),
            refresh_token=decrypt_token(token.refresh_token) if token.refresh_token else None,
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET
        )
        
        for email in user_emails:
            await execute_action_for_email(email, db, gmail_service)
            processed += 1
            
    return processed
