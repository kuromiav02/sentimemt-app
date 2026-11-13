# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- Avant (étape A) : 91 % (63/69 lignes), lignes jamais exécutées : `api/main.py:49`, `77–79` et `85–87`.
- `49` correspondait au 503 quand le modèle n'est pas chargé ; `77–79` aux erreurs levées pendant une prédiction ; `85–87` au lancement direct du module, que les tests exécutent via TestClient/Uvicorn.
- Après (étape D) : 100 % (82/82 lignes). Le bloc `if __name__ == "__main__"` est exclu avec `# pragma: no cover`, car les tests importent l'application et vérifient son démarrage avec TestClient plutôt que d'exécuter `api/main.py` comme script.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Une chaîne faite d'espaces passait `min_length`, mais le modèle la refusait avec une erreur non standard. | `test_frontieres_du_contrat` et `test_propriete_texte_tout_blanc_refuse` | Un validateur Pydantic applique `str.strip()` et produit une réponse 422 standard avant l'appel au modèle. |
| Un texte sans vocabulaire utile recevait tout de même une étiquette binaire. | `test_predict_texte_inconnu_s_abstient` | Le classifieur renvoie `INDETERMINE` sous le seuil d'abstention nommé. |
| Une `ValueError` du modèle pouvait être convertie à tort en 422, comme si la requête était invalide. | `test_panne_modele_repond_500_sans_details_internes` | Toute panne de prédiction, y compris `ValueError`, renvoie 500 sans exposer son message interne. |
| Le démarrage et les chemins de panne (modèle absent, non chargé ou classes inattendues) n'étaient pas couverts. | Les tests de `tests/test_integration.py` | Ajout de tests de cycle de vie, de disponibilité et de validation des classes du modèle. |

## 3. Seuil d'abstention

- Sur 58 avis de test : seuil `0,50` : 100 % de réponses, exactitude `0,879`, 7 erreurs ; seuil `0,60` : 72 % de réponses, exactitude `0,952`, 2 erreurs ; seuil `0,70` : 64 % de réponses, exactitude `1,000`, aucune erreur.
- Seuil retenu : `0,70` (`SEUIL_ABSTENTION`). À ce seuil, 21 avis sur 58 (36 %) sont transmis à un humain ; les 37 réponses automatiques du jeu de test sont exactes. Ce compromis évite les erreurs observées à `0,50–0,65` sans envoyer tous les avis en révision.

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : 20 avis (11 difficiles), 6 réponses justes, 14 abstentions, 0 erreur franche (donc 0 erreur déclarée comme connue).
- Les exemples difficiles et hors domaine sont souvent envoyés à un humain plutôt que classés à tort. Ce jeu écrit à la main complète les mesures de test, sans remplacer une évaluation représentative en production.

## 5. Outils statiques

- Au départ, `ruff check .` signalait 23 remarques dans l'espace de travail, dont des copies non versionnées des kits TP2–TP4 ; `mypy api` ne signalait rien, car les retours du modèle étaient des `dict` non typés.
- Aucun des défauts fonctionnels de la partie 2 n'avait été signalé par ruff ou mypy. Les types `TypedDict` et `Literal` rendent maintenant le contrat des étiquettes explicite ; les vérifications finales `ruff check .` et `mypy api` ne signalent aucune remarque.
