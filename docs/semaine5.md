# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface est un client HTTP et transmet les avis à l'API avec `POST /predict` ; elle ne charge ni le modèle ni son fichier. Le modèle peut ainsi être réentraîné ou remplacé côté API sans modifier la page, et l'interface n'a qu'un seul contrat à connaître.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Pour un texte inconnu comme « xqzvb wlkptr grombu », elle affiche « Je ne sais pas : à faire vérifier par un humain », la confiance (environ 52 %) et un rappel que la confiance est sous le seuil. Cela évite de présenter une prédiction peu fiable comme une certitude et permet à une personne de trancher.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Quand l'API est arrêtée, la page affiche « API injoignable : lancez d'abord uvicorn api.main:app » au lieu d'une erreur technique. Avec le modèle démo et le seuil d'abstention TP4 de 0,70, le fichier d'exemple produit 2 avis positifs, 2 négatifs et 2 à vérifier par un humain.
