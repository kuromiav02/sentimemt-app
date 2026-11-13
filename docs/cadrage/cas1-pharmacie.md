# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Une pharmacie souhaite assister ses préparateurs et pharmaciens en détectant automatiquement les éléments manquants ou non conformes sur les ordonnances médicales (posologie, durée, signature, identification du patient) pour sécuriser la délivrance.

## Utilisateur final (obligatoire)
Les préparateurs en pharmacie et les pharmaciens titulaires ou adjoints en officine qui reçoivent et analysent les ordonnances au comptoir ou en préparation.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [X] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Cette approche s'appuie sur la vérifiabilité (b) des exigences réglementaires : le système doit croiser le contenu extrait de l'ordonnance avec les bases de données officielles des médicaments et les recommandations légales, tout en sourçant précisément les règles manquantes. La conséquence d'une erreur (d) est critique (risque sanitaire), ce qui impose une traçabilité rigoureuse où chaque alerte est justifiée par un texte officiel ou un protocole de dispensation vérifiable par le pharmacien.

## Données nécessaires et leur origine (obligatoire)
Les nomenclatures officielles des médicaments, le Code de la santé publique relatif aux règles de prescription, ainsi qu'un corpus d'ordonnances anonymisées servant de cas de test pour valider la détection des champs obligatoires.

## Métrique de succès et seuil d'acceptation (obligatoire)
Un taux de rappel (sensibilité) supérieur à 98 % sur la détection des mentions obligatoires manquantes, garantissant qu'aucune omission critique ne passe inaperçue au comptoir.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une erreur de faux négatif (omission non détectée) peut entraîner la délivrance d'un traitement non conforme ou dangereux, tandis qu'un faux positif génère une alerte inutile. Le pharmacien conserve une validation humaine obligatoire et reste le seul décisionnaire final pour bloquer ou valider la délivrance de l'ordonnance.

## Risques éthiques ou de confidentialité (obligatoire)
Traitement de données de santé à caractère personnel (informations médicales et identifiants des patients), nécessitant un hébergement conforme (HDS / RGPD) et une stricte minimisation ou anonymisation des données traitées par les composants d'intelligence artificielle.

## Approche écartée et pourquoi (facultatif)
L'approche de type « Modèle génératif seul » a été écartée car elle présente un risque élevé d'hallucination, ce qui est inacceptable pour des vérifications réglementaires et sanitaires strictes où chaque règle doit être rigoureusement traçable.
