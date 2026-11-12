"""
Evidence ORM Model — stores fact-check evidence from external sources.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.database import Base


class Evidence(Base):
    """Stores a piece of fact-check evidence linked to a prediction."""

    __tablename__ = "evidences"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    prediction_id = Column(String, ForeignKey("predictions.id"), nullable=False)

    # Evidence details
    source = Column(String(200), nullable=False)  # e.g., "Google Fact Check", "Snopes"
    claim_reviewed = Column(Text, nullable=True)
    rating = Column(String(50), nullable=True)  # e.g., "False", "Mostly True"
    url = Column(String(2000), nullable=True)
    publisher = Column(String(200), nullable=True)
    review_date = Column(DateTime, nullable=True)
    relevance_score = Column(Float, nullable=True)  # 0.0 - 1.0

    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    prediction = relationship("Prediction", back_populates="evidences")

    def __repr__(self):
        return f"<Evidence(id={self.id}, source={self.source}, rating={self.rating})>"
