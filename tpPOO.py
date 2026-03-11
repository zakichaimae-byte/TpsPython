from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

class Boisson(ABC):
    """
    Classe abstraite représentant une boisson générique dans le café.
    """

    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def __add__(self, other):
        """Partie 4 : Combinaison de deux boissons"""
        if isinstance(other, Boisson):
            return BoissonCombinee(self, other)
        return NotImplemented

class BoissonCombinee(Boisson):
    """Classe interne pour gérer le résultat d'une addition de boissons"""
    def __init__(self, b1: Boisson, b2: Boisson):
        self.b1 = b1
        self.b2 = b2

    def cout(self) -> float:
        return self.b1.cout() + self.b2.cout()

    def description(self) -> str:
        return f"{self.b1.description()} + {self.b2.description()}"

# --- Partie 2 : Boissons concrètes ---

class Cafe(Boisson):
    def cout(self) -> float:
        return 10.0
    def description(self) -> str:
        return "Café"

class Thé(Boisson):
    def cout(self) -> float:
        return 8.0
    def description(self) -> str:
        return "Thé"

# --- Partie 3 : Ajout d'ingrédients (Décorateurs) ---

class DecorateurIngredient(Boisson):
    def __init__(self, boisson: Boisson):
        self._boisson = boisson

class Lait(DecorateurIngredient):
    def cout(self) -> float:
        return self._boisson.cout() + 2.0
    def description(self) -> str:
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurIngredient):
    def cout(self) -> float:
        return self._boisson.cout() + 1.0
    def description(self) -> str:
        return self._boisson.description() + ", Sucre"

class Caramel(DecorateurIngredient):
    def cout(self) -> float:
        return self._boisson.cout() + 3.0
    def description(self) -> str:
        return self._boisson.description() + ", Caramel"

# --- Partie 5 : Représentation d'un client ---

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

# --- Partie 7 : Gestion des commandes ---

class Commande:
    def __init__(self, client: Client):
        self.client = client
        self.boissons: List[Boisson] = []

    def ajouter_boisson(self, boisson: Boisson):
        self.boissons.append(boisson)

    def calculer_total(self) -> float:
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        print(f"Client : {self.client.nom} (N°{self.client.numero})")
        for b in self.boissons:
            print(f"- {b.description()} : {b.cout()} DH")
        print(f"Total : {self.calculer_total()} DH")

class CommandeSurPlace(Commande):
    def afficher(self):
        print("\n=== COMMANDE SUR PLACE ===")
        super().afficher()
        print("Installation en salle...")

class CommandeEmporter(Commande):
    def afficher(self):
        print("\n=== COMMANDE À EMPORTER ===")
        super().afficher()
        print("Préparation du sac et gobelets...")

class Fidelite:
    """Classe utilitaire pour la fidélité"""
    def ajouter_points(self, client: Client, montant: float):
        points = int(montant // 10) # 1 point par tranche de 10 DH
        client.points_fidelite += points
        print(f"Promotion : {points} points ajoutés à {client.nom}.")

class CommandeFidele(Commande, Fidelite):
    """Héritage multiple : Commande utilisant le système de fidélité"""
    def valider(self):
        total = self.calculer_total()
        self.ajouter_points(self.client, total)

if __name__ == "__main__":
    # 1. Création d'un client
    client1 = Client("Chaimae", 101)

    # 2. Création de boissons complexes
    cafe_special = Sucre(Lait(Cafe()))
    the_sucre = Sucre(Thé())

    # 3. Combinaison de boissons (Partie 4)
    combo = cafe_special + the_sucre

    # 4. Création d'une commande fidèle sur place
    commande = CommandeFidele(client1)
    commande.ajouter_boisson(combo)
    commande.ajouter_boisson(Caramel(Cafe()))

    # 5. Affichage
    # Utilisation du polymorphisme (si on avait une liste de commandes)
    print("\n--- Détails de la commande ---")
    commande.afficher()

    # 6. Validation et points de fidélité
    print("\n--- Validation ---")
    commande.valider()
    print(f"Points fidélité de {client1.nom} : {client1.points_fidelite}")


