"""
Explanation schemas for API responses.
"""

from datetime import datetime
from pydantic import BaseModel


class ExplanationResponse(BaseModel):
    """Schema for a SHAP/LIME explanation."""

    id: str
    prediction_id: str
    method: str  # "shap" or "lime"
    feature_importances: dict | None
    top_features: list[dict] | None
    narrative: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
