"""
Article schemas for request/response validation.
"""

from datetime import datetime
from pydantic import BaseModel, Field


class ArticleCreate(BaseModel):
    """Schema for creating a new article."""

    title: str | None = Field(None, max_length=500, description="Article headline or title")
    text: str = Field(..., min_length=10, description="Full article text or claim to analyze")
    language: str = Field("auto", pattern="^(en|hi|auto)$", description="Language: en, hi, or auto-detect")
    source_url: str | None = Field(None, max_length=2000, description="Original source URL")


class ArticleResponse(BaseModel):
    """Schema for article in API responses."""

    id: str
    title: str | None
    text: str
    language: str
    source_url: str | None
    submitted_at: datetime

    model_config = {"from_attributes": True}
