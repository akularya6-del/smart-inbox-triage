from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    
    NOTION_API_KEY: str | None = None
    NOTION_DATABASE_ID: str | None = None
    
    GOOGLE_CALENDAR_API_KEY: str | None = None
    
    ENCRYPTION_KEY: str = "default_unsafe_key_for_dev_only_123"
    
    SYNC_INTERVAL_MINUTES: int = 5
    SYNC_MAX_EMAILS: int = 50
    RETRY_ATTEMPTS: int = 6
    RETRY_DELAYS: List[int] = [1, 5, 15, 30, 60, 180]
    
    DATABASE_URL: str = "sqlite:///./data/app.db"
    
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    LOG_LEVEL: str = "INFO"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
