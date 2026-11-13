"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
from typing import Literal, TypedDict

from src.predict import charger_modele
from src.predict import predict as _predict

SEUIL_ABSTENTION = 0.70
ETIQUETTES_MODELE: dict[str, Literal["POSITIVE", "NEGATIVE"]] = {
    "positive": "POSITIVE",
    "negative": "NEGATIVE",
}


class ApiPrediction(TypedDict):
    label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        pipeline = charger_modele()
        classes = {str(label).lower() for label in pipeline.classes_}
        if classes != set(ETIQUETTES_MODELE):
            raise ValueError(f"Classes du modèle non prises en charge : {sorted(classes)}")

    def predict(self, text: str) -> ApiPrediction:
        """Renvoie le verdict, la confiance et un aperçu du texte."""
        prediction = _predict(text)
        mapped_label = ETIQUETTES_MODELE[prediction["label"]]
        label = mapped_label if prediction["score"] >= SEUIL_ABSTENTION else "INDETERMINE"
        return {"label": label, "score": prediction["score"], "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()
