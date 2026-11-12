"""
Analysis schemas — composed request/response for the full analysis pipeline.
"""

from pydantic import BaseModel, Field

from app.schemas.article import ArticleResponse
from app.schemas.prediction import PredictionResponse
from app.schemas.evidence import EvidenceResponse
from app.schemas.explanation import ExplanationResponse


class AnalysisRequest(BaseModel):
    """Schema for submitting text for analysis."""

    text: str = Field(..., min_length=10, description="Text or claim to analyze")
    title: str | None = Field(None, max_length=500, description="Optional title/headline")
    language: str = Field("auto", pattern="^(en|hi|auto)$", description="Language: en, hi, or auto")
    source_url: str | None = Field(None, description="Optional source URL")
    model: str = Field("ensemble", description="Model to use: fakebert, xlm-roberta, muril, ensemble")


class LinguisticFeatures(BaseModel):
    """Linguistic features extracted from the text."""

    word_count: int
    sentence_count: int
    avg_word_length: float
    avg_sentence_length: float
    punctuation_density: float
    caps_ratio: float
    exclamation_count: int
    question_count: int
    sentiment_polarity: float
    sentiment_subjectivity: float
    readability_score: float


class AnalysisResponse(BaseModel):
    """Quick analysis response (prediction only)."""

    article: ArticleResponse
    prediction: PredictionResponse


class FullAnalysisResponse(BaseModel):
    """Complete analysis response with evidence and explanations."""

    article: ArticleResponse
    prediction: PredictionResponse
    evidences: list[EvidenceResponse] = []
    explanations: list[ExplanationResponse] = []
    linguistic_features: LinguisticFeatures | None = None
