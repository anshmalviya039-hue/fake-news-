"""
Evidence schemas for API responses.
"""

from datetime import datetime
from pydantic import BaseModel, Field


class EvidenceResponse(BaseModel):
    """Schema for a single piece of fact-check evidence."""

    id: str
    prediction_id: str
    source: str
    claim_reviewed: str | None
    rating: str | None
    url: str | None
    publisher: str | None
    review_date: datetime | None
    relevance_score: float | None = Field(None, ge=0.0, le=1.0)
    created_at: datetime

    model_config = {"from_attributes": True}
