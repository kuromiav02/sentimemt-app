# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Une entreprise souhaite automatiser la priorisation et le routage des avis clients négatifs pour identifier et traiter en priorité absolue les réclamations les plus critiques.

## Utilisateur final (obligatoire)
Les équipes du service client et les responsables de la relation client qui gèrent les réclamations et la résolution des litiges.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [X] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Cette approche s'appuie sur l'exploitation d'un historique de données étiquetées (a) par le service client pour entraîner un modèle de classification de sévérité. Elle garantit également un faible coût par requête (c), indispensable pour traiter en temps réel et à grande échelle les flux massifs d'avis entrants.

## Données nécessaires et leur origine (obligatoire)
L'historique des avis clients et des tickets de support passés, annotés et classés selon leur niveau de criticité par les équipes opérationnelles.

## Métrique de succès et seuil d'acceptation (obligatoire)


## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un taux de rappel (sensibilité) supérieur à 90 % sur la détection des avis à haute criticité, afin de minimiser le risque de laisser sans réponse un client en situation de crise.

## Risques éthiques ou de confidentialité (obligatoire)
Une erreur de classification (faux négatif) retarde l'intervention sur un problème critique, tandis qu'un faux positif surcharge temporairement le support. Un conseiller humain conserve le contrôle final pour valider la priorisation et décider de l'action à mener.

## Approche écartée et pourquoi (facultatif)
L'approche par « Règles métier » a été écartée car la diversité, le sarcasme et la complexité du langage naturel dans les avis clients rendent les moteurs basés sur des mots-clés trop rigides et inefficaces.
