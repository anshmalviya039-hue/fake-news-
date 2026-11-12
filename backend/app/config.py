"""
Application configuration using Pydantic Settings.
Reads from .env file and environment variables.
"""

from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    # Application
    app_name: str = "Fake News Detection System"
    app_env: str = "development"
    debug: bool = True

    # Server
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    secret_key: str = "change-me-to-a-random-secret-key"

    # Database
    database_url: str = "sqlite:///./fake_news.db"

    # Google Fact Check API
    google_fact_check_api_key: str = ""

    # ML Models
    models_dir: str = str(Path(__file__).parent.parent.parent / "models")
    default_model: str = "ensemble"

    # CORS
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Cached settings instance."""
    return Settings()
