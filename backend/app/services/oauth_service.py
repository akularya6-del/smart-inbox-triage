import json
from datetime import datetime, timezone, timedelta
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from sqlalchemy.orm import Session
from app.config import settings
from app.models.user import User
from app.models.oauth_token import OAuthToken
from app.core.security import encrypt_token, decrypt_token
from app.core.exceptions import OAuthError

SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar.events'
]

# We must define the redirect URI for our backend.
# The frontend will hit this endpoint, or we return the URL and frontend redirects.
REDIRECT_URI = "http://localhost:3000/api/auth/callback/google" 

def _get_client_config() -> dict:
    if not settings.GOOGLE_CLIENT_ID or not settings.GOOGLE_CLIENT_SECRET:
        raise OAuthError("Google OAuth credentials are not configured.")
    return {
        "web": {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "project_id": "smart-triage",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": settings.GOOGLE_CLIENT_SECRET
        }
    }

def get_auth_url(state: str = None) -> dict:
    try:
        flow = Flow.from_client_config(
            _get_client_config(),
            scopes=SCOPES
        )
        flow.redirect_uri = REDIRECT_URI
        
        authorization_url, generated_state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            prompt='consent',
            state=state
        )
        return {"url": authorization_url, "state": generated_state}
    except Exception as e:
        raise OAuthError(f"Failed to generate auth URL: {str(e)}")

def exchange_code(code: str, db: Session) -> User:
    try:
        flow = Flow.from_client_config(
            _get_client_config(),
            scopes=SCOPES
        )
        flow.redirect_uri = REDIRECT_URI
        
        flow.fetch_token(code=code)
        credentials = flow.credentials
        
        # Get user info
        from googleapiclient.discovery import build
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()
        
        email = user_info.get("email")
        if not email:
            raise OAuthError("Could not retrieve email from Google.")
            
        # Check if user exists
        user = db.query(User).filter(User.email == email).first()
        if not user:
            user = User(
                email=email,
                name=user_info.get("name"),
                picture=user_info.get("picture")
            )
            db.add(user)
            db.flush()
            
        # Update or create token
        token = db.query(OAuthToken).filter(OAuthToken.user_id == user.id).first()
        if not token:
            token = OAuthToken(user_id=user.id)
            db.add(token)
            
        token.access_token = encrypt_token(credentials.token)
        if credentials.refresh_token:
            token.refresh_token = encrypt_token(credentials.refresh_token)
            
        token.expires_at = datetime.now(timezone.utc) + timedelta(seconds=credentials.expiry.timestamp() - datetime.now().timestamp() if credentials.expiry else 3600)
        
        db.commit()
        return user
    except Exception as e:
        db.rollback()
        raise OAuthError(f"Failed to exchange code: {str(e)}")
