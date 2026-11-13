# Semaine 3 : l'API, notes du binôme

> Deux questions, quelques phrases chacune. Répondez avec ce que vous avez observé, pas avec le cours.

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

Le test sans modèle provoque une `FileNotFoundError` dès le démarrage : l'API ne peut donc pas annoncer qu'elle est prête alors qu'aucune prédiction n'est possible. C'est une erreur de déploiement à corriger immédiatement ; un 503 est utile si le service tourne mais qu'une dépendance devient indisponible après le démarrage.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?

Les deux validations protègent des frontières différentes : Pydantic renvoie un 422 clair au client HTTP, tandis que `predict()` protège aussi les appels directs depuis Python. Cette défense en profondeur garde le contrat correct sans dépendre du chemin utilisé pour appeler le modèle.
