from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.oauth_service import get_auth_url, exchange_code
from app.core.exceptions import OAuthError
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])

class AuthStartResponse(BaseModel):
    url: str

class CallbackRequest(BaseModel):
    code: str

@router.get("/google/start", response_model=AuthStartResponse)
def start_oauth(request: Request):
    """Initiates the Google OAuth2 flow."""
    try:
        # In a real app we might store state in a session/cookie
        result = get_auth_url(state="frontend-state")
        return {"url": result["url"]}
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/google/callback")
def oauth_callback(body: CallbackRequest, db: Session = Depends(get_db)):
    """Handles the OAuth callback, trading code for token."""
    try:
        user = exchange_code(body.code, db)
        return {"status": "success", "user_id": user.id, "email": user.email}
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/disconnect")
def disconnect_oauth(user_id: str, db: Session = Depends(get_db)):
    """Disconnects the user's Google account and revokes tokens."""
    # In a real app user_id comes from auth middleware/token
    from app.models.oauth_token import OAuthToken
    token = db.query(OAuthToken).filter(OAuthToken.user_id == user_id).first()
    if token:
        db.delete(token)
        db.commit()
    return {"status": "success", "message": "Account disconnected"}
