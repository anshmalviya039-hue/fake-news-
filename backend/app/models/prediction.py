"""
Prediction ORM Model — stores classification results.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.database import Base


class Prediction(Base):
    """Stores a classification prediction for an article."""

    __tablename__ = "predictions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    article_id = Column(String, ForeignKey("articles.id"), nullable=False)

    # Classification result
    verdict = Column(String(20), nullable=False)  # "real", "fake", "uncertain"
    confidence = Column(Float, nullable=False)  # 0.0 - 1.0
    model_used = Column(String(50), nullable=False)  # e.g., "fakebert", "ensemble"

    # Metadata
    processing_time_ms = Column(Float, nullable=True)
    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    article = relationship("Article", back_populates="predictions")
    evidences = relationship(
        "Evidence", back_populates="prediction", cascade="all, delete-orphan"
    )
    explanations = relationship(
        "Explanation", back_populates="prediction", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Prediction(id={self.id}, verdict={self.verdict}, confidence={self.confidence:.2f})>"
