# Analyseur de Notes et de Cohérence Pédagogique (TP 1)

Ce fichier `tp1.py` contient la résolution du TP numéro 1.

L'objectif de ce script est de traiter des sous-ensembles de données (représentant des notes d'étudiants). Il démontre l'utilisation des structures de données natives en Python :
- Tuple
- Liste
- Dictionnaire
- Set

## Contenu du script

1. **Nettoyage et validation** (`valider`) : Vérifier la cohérence d'une ligne (nom, matière, groupe, note numérique 0-20). Sépare les tuples en valides, erreurs, et écarte les doublons parfaits.
2. **Structuration** : Organisation hiérarchique : `Etudiant -> Matière -> Liste de notes`. Identifier les matières de manière unique et regrouper les étudiants par `Groupe`.
3. **Calculs** : Implémentation d'une fonction récursive `somme_recursive` pour calculer des moyennes (générales et par matière).
4. **Analyse avancée** : Système de listage d'alertes :
   - Multiples notes pour la même matière
   - Profils étudiants incomplets (n'ayant pas toutes les matières de son cursus)
   - Groupes présentant une moyenne trop faible
   - Écarts importants (ex: 5 points ou plus) entre la pire et la meilleure note d'un étudiant.

## Exécution

Ouvrir un terminal dans ce dossier et exécuter :

```bash
python tp1.py
```
