# Travaux Pratiques Python - LP Génie Logiciel

Ce dépôt contient les rendus des Travaux Pratiques réalisés en Python.

## [TP 1] Analyseur de Notes et de Cohérence Pédagogique

Le fichier `tp1.py` contient la résolution du premier TP axé sur les structures de données natives en Python.

**Objectifs :** Traiter des sous-ensembles de données (représentant des notes d'étudiants).
- **Structures de données :** Utilisation de Tuples, Listes, Dictionnaires et Sets.
- **Fonctionnalités :** 
  - Nettoyage et validation des données d'entrée.
  - Structuration hiérarchique (`Etudiant -> Matière -> Liste de notes`).
  - Calculs de moyennes via une fonction récursive `somme_recursive`.
  - Analyse avancée et levée d'alertes (doublons, profils incomplets, groupes faibles, écarts de notes).

## [TP 2] Système de Gestion de Boissons - Café (POO)

Le fichier `tpPOO.py` contient la résolution du second TP axé sur la Programmation Orientée Objet (POO).

**Objectifs :** Concevoir un système de commandes pour un café en respectant les principes SOLID et plusieurs design patterns.
- **Concepts couverts :**
  - **Abstraction :** Classe de base `Boisson`.
  - **Design Pattern Décorateur :** Ajout dynamique d'ingrédients (`Lait`, `Sucre`, `Caramel`) sans modifier les classes concrètes de boissons.
  - **Surcharge d'opérateur :** Redéfinition de l'opérateur `+` (`__add__`) pour combiner des boissons en menus.
  - **Data Classes :** Utilisation de `@dataclass` pour modéliser les informations `Client`.
  - **Polymorphisme & Héritage Multiple :** Spécialisation des commandes (`SurPlace`, `Emporter`) et création de `CommandeFidele` héritant à la fois de `Commande` et du mix-in `Fidelite`.

Le code complet et documenté est disponible dans `tpPOO.py`, et le rapport descriptif du système dans `Rapport_TP2_POO.md` (ou `.docx`).

---
## Exécution des scripts

Ouvrir un terminal dans ce dossier et exécuter le TP souhaité :

```bash
# Pour le TP 1
python tp1.py

# Pour le TP 2
python tpPOO.py
```
