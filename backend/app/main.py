"""
FastAPI Application Entry Point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.models.database import create_tables
from app.api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events."""
    # Startup: create database tables
    create_tables()
    print("✅ Database tables created")
    print("🚀 Fake News Detection System is ready!")
    yield
    # Shutdown
    print("👋 Shutting down...")


def create_app() -> FastAPI:
    """Application factory."""
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        description=(
            "AI-Powered Multilingual Fake News Detection & Evidence Verification System. "
            "Combines classical ML, transformer models (FakeBERT, XLM-RoBERTa, MuRIL), "
            "explainable AI (SHAP/LIME), and evidence retrieval."
        ),
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(api_router, prefix="/api")

    return app


# Create app instance
app = create_app()
