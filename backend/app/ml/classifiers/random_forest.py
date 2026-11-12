"""
Random Forest classifier wrapper.
"""

from typing import Any
from sklearn.ensemble import RandomForestClassifier as SklearnRF

from app.ml.classifiers.base import BaseClassifier


class RandomForestClassifier(BaseClassifier):
    """Random Forest wrapper with standardized interface."""

    def __init__(self, **kwargs):
        super().__init__(name="random_forest")
        self.model = self.build_model(**kwargs)

    def build_model(self, **kwargs) -> Any:
        """Build RandomForestClassifier with sensible defaults."""
        defaults = {
            "n_estimators": 200,
            "max_depth": None,
            "min_samples_split": 5,
            "random_state": 42,
            "n_jobs": -1,
        }
        defaults.update(kwargs)
        return SklearnRF(**defaults)
