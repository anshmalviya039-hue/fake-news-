"""
Prediction schemas for API responses.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class VerdictEnum(str, Enum):
    """Possible prediction verdicts."""
    REAL = "real"
    FAKE = "fake"
    UNCERTAIN = "uncertain"


class PredictionResponse(BaseModel):
    """Schema for a prediction result."""

    id: str
    article_id: str
    verdict: VerdictEnum
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score 0-1")
    model_used: str
    processing_time_ms: float | None
    created_at: datetime

    model_config = {"from_attributes": True}
