# Travaux Pratiques Python

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

## [TP Django] Installation et Architecture de Base

Le dossier `tp_django_project` est un projet de base Django complet réalisé selon l'architecture **MVT (Modèle-Vue-Template)**.

**Objectifs :** Configurer un environnement Django, manipuler des templates, créer des modèles et gérer l'authentification.
- **Fonctionnalités :** 
  - Système d'authentification utilisateur robuste (Inscription, Connexion, Déconnexion).
  - Un compteur de mots dynamique (`counter`) avec requête `POST` sécurisée par un jeton `CSRF`.
  - Intégration de modèles (`Feature`) gérables depuis l'interface administrateur Django et affichés sur la page d'accueil.
  - Design premium et responsive via une refonte UI/UX sur mesure des vues HTML.

Le code complet source se trouve dans `tp_django_project/myproject`, et le rapport explicatif détaillé des étapes de création est disponible dans `Rapport_TP_Django.md` (ou `.docx`).

---
## Exécution des scripts

Ouvrir un terminal dans ce dossier et exécuter le TP souhaité :

```bash
# Pour le TP 1
python tp1.py

# Pour le TP 2
python tpPOO.py

# Pour le TP Django (nécessite le lancement du serveur)
cd tp_django_project/myproject
python manage.py runserver
# Puis ouvrez http://127.0.0.1:8000
```
