"""
Article ORM Model — stores submitted news articles/claims.
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.orm import relationship

from app.models.database import Base


class Article(Base):
    """Represents a submitted news article or claim."""

    __tablename__ = "articles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(500), nullable=True)
    text = Column(Text, nullable=False)
    language = Column(String(10), nullable=False, default="en")  # en, hi, auto
    source_url = Column(String(2000), nullable=True)
    submitted_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    predictions = relationship(
        "Prediction", back_populates="article", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Article(id={self.id}, language={self.language}, title={self.title[:50] if self.title else 'N/A'})>"
