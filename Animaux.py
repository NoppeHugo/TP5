class Animal:
    def __init__(self, tete, corps, membres, habitat):
        self.tete = tete
        self.corps = corps
        self.membres = membres
        self.habitat = habitat


    def afficher(self):
        return f"Tête : {self.tete}, Corps : {self.corps}, Membres : {self.membres}, Habitat : {self.habitat}"


class Herbivore(Animal):
    def __init__(self, tete, corps, membres, habitat, type_herbivore):
        super().__init__(tete, corps, membres, habitat)
        self.type_herbivore = type_herbivore

    def manger_plantes(self):
        return f"{self.type_herbivore} mange des plantes."


class Carnivore(Animal):
    def __init__(self, tete, corps, membres, habitat, type_carnivore):
        super().__init__(tete, corps, membres, habitat)
        self.type_carnivore = type_carnivore

    def manger_viande(self):
        return f"{self.type_carnivore} mange de la viande."


# Exemple d'utilisation
lapin = Herbivore("Petite tête", "Corps poilu", 4, "Forêt", "Lapin")
mouton = Herbivore("Tête laineuse", "Corps laineux", 4, "Prairie", "Mouton")
lion = Carnivore("Tête imposante", "Corps musclé", 4, "Savane", "Lion")

print(lapin.afficher())
print(lapin.manger_plantes())
print(mouton.afficher())
print(mouton.manger_plantes())
print(lion.afficher())
print(lion.manger_viande())

try:
    print(lapin.manger_viande())
except AttributeError as e: 
    print(e)

