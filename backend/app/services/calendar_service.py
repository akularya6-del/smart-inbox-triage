from app.config import settings
from app.core.exceptions import ActionExecutionError
from app.services.gmail_service import GmailService
import structlog
from datetime import datetime, timedelta

logger = structlog.get_logger(__name__)

def create_calendar_event(title: str, description: str, gmail_service: GmailService):
    """Creates a 30-min Google Calendar event tomorrow at 10 AM as a reminder."""
    # Since we use the user's Gmail OAuth token which has calendar scopes, 
    # we can use the same google-api-client credentials.
    
    service = gmail_service.credentials
    # We would build the calendar service here
    from googleapiclient.discovery import build
    calendar = build('calendar', 'v3', credentials=service)
    
    # Simple logic: Tomorrow at 10 AM
    start_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0) + timedelta(days=1)
    end_time = start_time + timedelta(minutes=30)
    
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat() + 'Z',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
        },
    }
    
    try:
        created = calendar.events().insert(calendarId='primary', body=event).execute()
        return created.get('id')
    except Exception as e:
        logger.error(f"Failed to create calendar event: {str(e)}")
        raise ActionExecutionError(f"Calendar API error: {str(e)}")
