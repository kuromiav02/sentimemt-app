"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D).

Les tests du TP3 vérifient des réponses ; ceux-ci vérifient le démarrage de l'API
et son comportement quand le modèle manque ou tombe en panne.
"""
import pytest


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_demarrage_refuse_si_modele_absent(monkeypatch, tmp_path):
    from fastapi.testclient import TestClient

    import src.predict as tp2_predict
    from api.main import app

    monkeypatch.setattr(tp2_predict, "MODELE", tmp_path / "absent.joblib")
    tp2_predict.charger_modele.cache_clear()
    try:
        with pytest.raises(FileNotFoundError, match="sentiment.joblib absent"):
            with TestClient(app):
                pass
    finally:
        tp2_predict.charger_modele.cache_clear()


def test_modele_non_charge_repond_503(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier")
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "avis valable"}).status_code == 503


@pytest.mark.parametrize("erreur", [RuntimeError("panne runtime"), ValueError("bug interne")])
def test_panne_modele_repond_500_sans_details_internes(monkeypatch, erreur):
    from fastapi.testclient import TestClient

    from api.main import app

    class ModeleEnPanne:
        def predict(self, text: str):
            raise erreur

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", ModeleEnPanne())
        reponse = client.post("/predict", json={"text": "avis valable"})
    assert reponse.status_code == 500
    assert "Erreur interne du serveur" == reponse.json()["detail"]
    assert str(erreur) not in reponse.text


def test_demarrage_refuse_classes_modele_inattendues(monkeypatch):
    from fastapi.testclient import TestClient

    import api.model as api_model
    from api.main import app

    class ModeleClassesInattendues:
        classes_ = ["negative", "neutral", "positive"]

    monkeypatch.setattr(api_model, "charger_modele", lambda: ModeleClassesInattendues())
    with pytest.raises(ValueError, match="Classes du modèle non prises en charge"):
        with TestClient(app):
            pass
