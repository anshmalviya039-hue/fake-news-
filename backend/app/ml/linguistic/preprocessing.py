"""
Text preprocessing utilities for the fake news detection pipeline.
Handles cleaning, tokenization, and language detection.
"""

import re
import string

from langdetect import detect, LangDetectException


def clean_text(text: str) -> str:
    """
    Clean and normalize input text.

    Steps:
    - Remove URLs
    - Remove HTML tags
    - Normalize whitespace
    - Strip leading/trailing whitespace

    Args:
        text: Raw input text.

    Returns:
        Cleaned text string.
    """
    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def remove_special_characters(text: str, keep_punctuation: bool = True) -> str:
    """
    Remove special characters from text.

    Args:
        text: Input text.
        keep_punctuation: If True, keeps standard punctuation.

    Returns:
        Text with special characters removed.
    """
    if keep_punctuation:
        # Keep alphanumeric, spaces, and basic punctuation
        pattern = r"[^a-zA-Z0-9\s" + re.escape(string.punctuation) + r"\u0900-\u097F]"
    else:
        # Keep only alphanumeric, spaces, and Devanagari characters
        pattern = r"[^a-zA-Z0-9\s\u0900-\u097F]"

    return re.sub(pattern, "", text)


def detect_language(text: str) -> str:
    """
    Detect the language of the input text.

    Args:
        text: Input text.

    Returns:
        ISO 639-1 language code (e.g., 'en', 'hi').
        Returns 'en' as fallback if detection fails.
    """
    try:
        lang = detect(text)
        # Map to supported languages
        if lang == "hi":
            return "hi"
        return "en"  # Default to English for all non-Hindi
    except LangDetectException:
        return "en"


def tokenize_simple(text: str) -> list[str]:
    """
    Simple whitespace tokenizer.

    Args:
        text: Input text.

    Returns:
        List of tokens.
    """
    return text.split()


def truncate_text(text: str, max_length: int = 512) -> str:
    """
    Truncate text to a maximum number of words.

    Args:
        text: Input text.
        max_length: Maximum number of words.

    Returns:
        Truncated text.
    """
    words = text.split()
    if len(words) <= max_length:
        return text
    return " ".join(words[:max_length])
