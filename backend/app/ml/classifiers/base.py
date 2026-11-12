"""
Abstract base class for all classical ML classifiers.
Provides a common interface for training, prediction, saving, and loading.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import numpy as np
import joblib


class BaseClassifier(ABC):
    """
    Abstract base class for classical ML classifiers.

    All classifier wrappers (LogisticRegression, RandomForest, XGBoost)
    must implement this interface.
    """

    def __init__(self, name: str, model: Any = None):
        self.name = name
        self.model = model
        self.is_fitted = False

    @abstractmethod
    def build_model(self, **kwargs) -> Any:
        """
        Build and return the underlying sklearn/xgboost model.

        Args:
            **kwargs: Model-specific hyperparameters.

        Returns:
            Configured model instance.
        """
        pass

    def train(self, X: np.ndarray, y: np.ndarray, **kwargs) -> dict:
        """
        Train the model on the given data.

        Args:
            X: Feature matrix (n_samples, n_features).
            y: Target labels (n_samples,).
            **kwargs: Additional training parameters.

        Returns:
            Dictionary with training metrics.
        """
        if self.model is None:
            self.model = self.build_model(**kwargs)

        self.model.fit(X, y)
        self.is_fitted = True

        # Compute training accuracy
        train_accuracy = self.model.score(X, y)
        return {"train_accuracy": train_accuracy}

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels.

        Args:
            X: Feature matrix (n_samples, n_features).

        Returns:
            Predicted labels (n_samples,).
        """
        if not self.is_fitted:
            raise RuntimeError(f"Model '{self.name}' is not fitted. Call train() first.")
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class probabilities.

        Args:
            X: Feature matrix (n_samples, n_features).

        Returns:
            Class probabilities (n_samples, n_classes).
        """
        if not self.is_fitted:
            raise RuntimeError(f"Model '{self.name}' is not fitted. Call train() first.")
        return self.model.predict_proba(X)

    def save(self, path: str | Path) -> None:
        """
        Save the trained model to disk.

        Args:
            path: File path to save the model.
        """
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, path)
        print(f"💾 Model '{self.name}' saved to {path}")

    def load(self, path: str | Path) -> None:
        """
        Load a trained model from disk.

        Args:
            path: File path to load the model from.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Model file not found: {path}")
        self.model = joblib.load(path)
        self.is_fitted = True
        print(f"📂 Model '{self.name}' loaded from {path}")

    def __repr__(self):
        status = "fitted" if self.is_fitted else "not fitted"
        return f"<{self.__class__.__name__}(name='{self.name}', {status})>"
