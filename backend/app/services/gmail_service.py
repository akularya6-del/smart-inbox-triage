from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.core.exceptions import GmailSyncError
import structlog

logger = structlog.get_logger(__name__)

class GmailService:
    def __init__(self, access_token: str, refresh_token: str, client_id: str, client_secret: str):
        self.credentials = Credentials(
            token=access_token,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret
        )
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def get_messages_list(self, max_results: int = 50, page_token: str = None, query: str = "is:unread"):
        """Fetch list of message IDs"""
        try:
            results = self.service.users().messages().list(
                userId='me',
                maxResults=max_results,
                pageToken=page_token,
                q=query
            ).execute()
            return results
        except HttpError as error:
            logger.error("Failed to fetch messages list", error=str(error))
            raise GmailSyncError(f"Gmail API error: {error}")

    def get_message(self, msg_id: str):
        """Fetch full message details"""
        try:
            return self.service.users().messages().get(
                userId='me',
                id=msg_id,
                format='full'
            ).execute()
        except HttpError as error:
            logger.error(f"Failed to fetch message {msg_id}", error=str(error))
            raise GmailSyncError(f"Gmail API error: {error}")

    def mark_as_read(self, msg_id: str):
        """Remove UNREAD label"""
        try:
            return self.service.users().messages().modify(
                userId='me',
                id=msg_id,
                body={'removeLabelIds': ['UNREAD']}
            ).execute()
        except HttpError as error:
            logger.error(f"Failed to mark message {msg_id} as read", error=str(error))
            raise GmailSyncError(f"Gmail API error: {error}")
