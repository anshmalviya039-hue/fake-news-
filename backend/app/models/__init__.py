"""
Database Models Package
"""

from app.models.database import Base, get_db, create_tables
from app.models.article import Article
from app.models.prediction import Prediction
from app.models.evidence import Evidence
from app.models.explanation import Explanation

__all__ = [
    "Base",
    "get_db",
    "create_tables",
    "Article",
    "Prediction",
    "Evidence",
    "Explanation",
]
