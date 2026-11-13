# sentiment-app : dépôt du binôme

Application fil rouge du cours *Développement et déploiement d'applications intelligentes*.
Ce dépôt grandit chaque semaine ; la semaine 1 met en place le cadrage et l'environnement.

## Installation (3 commandes)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell : .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Vérifier son installation

```bash
python scripts/check_setup.py    # diagnostic lisible : versions, dossiers, Git
pytest -q                        # mêmes vérifications sous forme de tests
```

La démarche complète de test, étape par étape, est dans `TESTS.md`.

## Structure

```text
sentiment-app/
├── README.md
├── TP1-ENONCE.md    # énoncé du TP de la semaine 1
├── TESTS.md         # démarche à suivre pour le test
├── requirements.txt
├── .gitignore
├── data/            # jeux de données (versionnés par DVC à partir de la semaine 7)
├── models/          # modèles entraînés (jamais dans Git)
├── api/             # API FastAPI (semaine 3)
├── src/             # génération, entraînement, évaluation et prédiction
├── ui/              # Streamlit (semaine 5)
├── tests/           # tests pytest
├── scripts/         # utilitaires (check_setup, nouveau cas de cadrage)
└── docs/            # cadrage et comptes rendus des TP
```

## Lancer l'API de sentiment (semaine 3)

Après avoir installé les dépendances et entraîné le modèle (`python src/train.py`) :

```bash
uvicorn api.main:app --reload
```

L'API est disponible à `http://localhost:8000` et sa documentation interactive à `http://localhost:8000/docs`.

## Lancer l'interface Streamlit (semaine 5)

Dans un second terminal, avec l'environnement virtuel activé :

```bash
streamlit run ui/app.py
```

La page s'ouvre à `http://localhost:8501` et utilise l'API déjà démarrée dans le premier terminal.

## Membres du binôme

| Rôle | Nom | Identifiant GitHub | Travail de la semaine 1 |
| --- | --- | --- | --- |
| Membre A | [Nom 1] | [@login] | |
| Membre B | [Nom 2] | [@login] | |
