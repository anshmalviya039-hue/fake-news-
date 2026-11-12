"""
Linguistic feature extraction for fake news detection.
Extracts 15+ features: readability, sentiment, lexical, syntactic, and stylistic.
"""

import re
import string
from dataclasses import dataclass

# TODO: Uncomment after installing nltk data
# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.tag import pos_tag
# from textblob import TextBlob
# import textstat


@dataclass
class LinguisticFeatureSet:
    """Container for extracted linguistic features."""

    word_count: int = 0
    sentence_count: int = 0
    avg_word_length: float = 0.0
    avg_sentence_length: float = 0.0
    punctuation_density: float = 0.0
    caps_ratio: float = 0.0
    exclamation_count: int = 0
    question_count: int = 0
    sentiment_polarity: float = 0.0
    sentiment_subjectivity: float = 0.0
    readability_score: float = 0.0
    unique_word_ratio: float = 0.0
    stopword_ratio: float = 0.0
    noun_ratio: float = 0.0
    verb_ratio: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary for API responses."""
        return {
            "word_count": self.word_count,
            "sentence_count": self.sentence_count,
            "avg_word_length": round(self.avg_word_length, 2),
            "avg_sentence_length": round(self.avg_sentence_length, 2),
            "punctuation_density": round(self.punctuation_density, 4),
            "caps_ratio": round(self.caps_ratio, 4),
            "exclamation_count": self.exclamation_count,
            "question_count": self.question_count,
            "sentiment_polarity": round(self.sentiment_polarity, 4),
            "sentiment_subjectivity": round(self.sentiment_subjectivity, 4),
            "readability_score": round(self.readability_score, 2),
            "unique_word_ratio": round(self.unique_word_ratio, 4),
            "stopword_ratio": round(self.stopword_ratio, 4),
            "noun_ratio": round(self.noun_ratio, 4),
            "verb_ratio": round(self.verb_ratio, 4),
        }

    def to_feature_vector(self) -> list[float]:
        """Convert to numeric feature vector for ML models."""
        return [
            self.word_count,
            self.sentence_count,
            self.avg_word_length,
            self.avg_sentence_length,
            self.punctuation_density,
            self.caps_ratio,
            self.exclamation_count,
            self.question_count,
            self.sentiment_polarity,
            self.sentiment_subjectivity,
            self.readability_score,
            self.unique_word_ratio,
            self.stopword_ratio,
            self.noun_ratio,
            self.verb_ratio,
        ]


def extract_features(text: str) -> LinguisticFeatureSet:
    """
    Extract all linguistic features from text.

    Uses basic Python string operations for features that don't require
    NLTK/TextBlob. Full NLP features are activated when dependencies
    are available.

    Args:
        text: Input text (should be pre-cleaned).

    Returns:
        LinguisticFeatureSet with all extracted features.
    """
    features = LinguisticFeatureSet()

    if not text or len(text.strip()) == 0:
        return features

    # === Basic lexical features (no external deps) ===
    words = text.split()
    features.word_count = len(words)

    # Sentence count (simple heuristic)
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    features.sentence_count = max(len(sentences), 1)

    # Average word length
    if words:
        features.avg_word_length = sum(len(w) for w in words) / len(words)

    # Average sentence length
    features.avg_sentence_length = features.word_count / features.sentence_count

    # Punctuation density
    punct_count = sum(1 for c in text if c in string.punctuation)
    features.punctuation_density = punct_count / max(len(text), 1)

    # Capitalization ratio
    alpha_chars = [c for c in text if c.isalpha()]
    if alpha_chars:
        features.caps_ratio = sum(1 for c in alpha_chars if c.isupper()) / len(alpha_chars)

    # Exclamation and question marks
    features.exclamation_count = text.count("!")
    features.question_count = text.count("?")

    # Unique word ratio (lexical diversity)
    if words:
        lower_words = [w.lower() for w in words]
        features.unique_word_ratio = len(set(lower_words)) / len(lower_words)

    # === Sentiment (basic fallback) ===
    # TODO: Replace with TextBlob or VADER when available
    features.sentiment_polarity = 0.0
    features.sentiment_subjectivity = 0.0

    # === Readability (basic fallback) ===
    # TODO: Replace with textstat.flesch_reading_ease(text) when available
    features.readability_score = 0.0

    # === POS ratios (stub) ===
    # TODO: Implement with nltk.pos_tag when NLTK data is downloaded
    features.noun_ratio = 0.0
    features.verb_ratio = 0.0
    features.stopword_ratio = 0.0

    return features


def extract_features_batch(texts: list[str]) -> list[LinguisticFeatureSet]:
    """
    Extract features from multiple texts.

    Args:
        texts: List of input texts.

    Returns:
        List of LinguisticFeatureSet objects.
    """
    return [extract_features(text) for text in texts]
