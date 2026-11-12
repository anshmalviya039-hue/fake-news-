"""
Explanation ORM Model — stores SHAP/LIME explainability results.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.models.database import Base


class Explanation(Base):
    """Stores an explainability result (SHAP or LIME) for a prediction."""

    __tablename__ = "explanations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    prediction_id = Column(String, ForeignKey("predictions.id"), nullable=False)

    # Explanation details
    method = Column(String(20), nullable=False)  # "shap" or "lime"
    feature_importances = Column(JSON, nullable=True)  # {"feature_name": importance_value, ...}
    top_features = Column(JSON, nullable=True)  # [{"feature": "word_count", "importance": 0.85}, ...]
    narrative = Column(Text, nullable=True)  # Human-readable explanation

    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    prediction = relationship("Prediction", back_populates="explanations")

    def __repr__(self):
        return f"<Explanation(id={self.id}, method={self.method})>"
