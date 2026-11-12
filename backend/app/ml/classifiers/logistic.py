"""
Logistic Regression classifier wrapper.
"""

from typing import Any
from sklearn.linear_model import LogisticRegression

from app.ml.classifiers.base import BaseClassifier


class LogisticRegressionClassifier(BaseClassifier):
    """Logistic Regression wrapper with standardized interface."""

    def __init__(self, **kwargs):
        super().__init__(name="logistic_regression")
        self.model = self.build_model(**kwargs)

    def build_model(self, **kwargs) -> Any:
        """Build LogisticRegression with sensible defaults."""
        defaults = {
            "max_iter": 1000,
            "random_state": 42,
            "C": 1.0,
            "solver": "lbfgs",
            "n_jobs": -1,
        }
        defaults.update(kwargs)
        return LogisticRegression(**defaults)
