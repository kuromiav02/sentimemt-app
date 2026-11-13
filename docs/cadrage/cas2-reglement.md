# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Offrir aux collaborateurs un assistant virtuel interactif capable d'apporter des réponses instantanées, précises et directement sourcées sur le règlement intérieur et les politiques RH de l'organisation.

## Utilisateur final (obligatoire)
Les employés de l'entreprise ainsi que les équipes des ressources humaines souhaitant traiter rapidement les demandes d'information courantes.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [X] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Le RAG garantit une stricte vérifiabilité (b) en associant chaque réponse générée à la citation explicite de l'article exact du règlement intérieur. La conséquence d'une erreur (d) étant importante sur le plan juridique et RH, l'ancrage documentaire est indispensable pour proscrire toute hallucination du modèle, tout en réduisant le besoin en données étiquetées (a) puisqu'il exploite directement les textes d'entreprise existants.

## Données nécessaires et leur origine (obligatoire)
Le règlement intérieur officiel à jour, les chartes internes (télétravail, sécurité, éthique) et les fiches pratiques RH fournies par la direction des ressources humaines.

## Métrique de succès et seuil d'acceptation (obligatoire)
Un taux de fidélité documentaire (exactitude des citations et absente d'hallucination) d'au moins 95 % sur un jeu de test de questions RH types.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une mauvaise information peut induire le salarié en erreur sur ses droits ou obligations (ex. procédure disciplinaire, congés). Un bouton d'escalade vers le service RH permet une validation humaine directe pour toute question ambiguë ou contestation.

## Risques éthiques ou de confidentialité (obligatoire)
Risque lié au traitement de questions contenant des données personnelles sensibles ou confidentielles d'un employé, nécessitant l'anonymisation des requêtes avant transmission au modèle et l'absence de conservation des historiques nominatifs.

## Approche écartée et pourquoi (facultatif)
L'approche « Modèle génératif seul » a été écartée car elle expose à des hallucinations réglementaires et ne permet pas d'assurer la traçabilité par citation des textes officiels de l'entreprise.
