# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Une entreprise souhaite automatiser la priorisation et le routage des avis clients négatifs pour identifier et traiter en priorité absolue les réclamations les plus critiques.

## Utilisateur final (obligatoire)
Les équipes du service client et les responsables de la relation client qui gèrent les réclamations et la résolution des litiges.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Cette approche s'appuie sur l'exploitation d'un historique de données étiquetées (a) par le service client pour entraîner un modèle de classification de sévérité. Elle garantit également un faible coût par requête (c), indispensable pour traiter en temps réel et à grande échelle les flux massifs d'avis entrants.

## Données nécessaires et leur origine (obligatoire)
L'historique des avis clients et des tickets de support passés, annotés et classés selon leur niveau de criticité par les équipes opérationnelles.

## Métrique de succès et seuil d'acceptation (obligatoire)
Un rappel supérieur à 90 % sur les avis à haute criticité est le seuil d'acceptation, afin de minimiser les réclamations urgentes non détectées. La mesure sera calculée sur un jeu de test annoté par le service client.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un faux négatif peut retarder la prise en charge d'un client en difficulté, tandis qu'un faux positif mobilise inutilement un conseiller. Un conseiller humain vérifie les avis prioritaires et décide de l'action à mener.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des données personnelles et des propos sensibles ; leur accès doit être limité et leur conservation réduite au nécessaire. Les annotations et les résultats seront surveillés pour repérer les biais entre groupes de clients.

## Approche écartée et pourquoi (facultatif)
L'approche par « Règles métier » a été écartée car la diversité, le sarcasme et la complexité du langage naturel dans les avis clients rendent les moteurs basés sur des mots-clés trop rigides et inefficaces.
