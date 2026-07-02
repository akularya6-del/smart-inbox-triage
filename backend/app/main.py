from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import structlog

from app.config import settings
from app.core.logging import setup_logging

logger = structlog.get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Application starting up")
    start_scheduler()
    yield
    logger.info("Application shutting down")

app = FastAPI(
    title="Smart Inbox Triage Dashboard",
    description="API for managing email classification, rules, and actions",
    version="0.1.0",
    lifespan=lifespan
)

from app.api.auth import router as auth_router
from app.api.emails import router as emails_router
from app.api.rules import router as rules_router
from app.api.review import router as review_router
from app.api.jobs import router as jobs_router

app.include_router(auth_router, prefix="/api")
app.include_router(emails_router, prefix="/api")
app.include_router(rules_router, prefix="/api")
app.include_router(review_router, prefix="/api")
app.include_router(jobs_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": app.version}
