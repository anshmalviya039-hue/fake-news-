"""
XGBoost classifier wrapper.
"""

from typing import Any
from xgboost import XGBClassifier

from app.ml.classifiers.base import BaseClassifier


class XGBoostClassifier(BaseClassifier):
    """XGBoost wrapper with standardized interface."""

    def __init__(self, **kwargs):
        super().__init__(name="xgboost")
        self.model = self.build_model(**kwargs)

    def build_model(self, **kwargs) -> Any:
        """Build XGBClassifier with sensible defaults."""
        defaults = {
            "n_estimators": 300,
            "max_depth": 6,
            "learning_rate": 0.1,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "random_state": 42,
            "use_label_encoder": False,
            "eval_metric": "logloss",
            "n_jobs": -1,
        }
        defaults.update(kwargs)
        return XGBClassifier(**defaults)
