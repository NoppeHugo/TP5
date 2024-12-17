class Classe:
    def __init__(self, professeur):
        self.professeur = professeur
        self.eleves = []

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            raise ValueError("La classe est pleine.")

    def afficher_classe(self):
        prof_info = f"Professeur: {self.professeur.afficher_dossier()}"
        eleve_infos = "\n".join([eleve.afficher_dossier() for eleve in self.eleves])
        return f"{prof_info}\nÉlèves:\n{eleve_infos if eleve_infos else 'Aucun élève'}"
    
class Dossier:
    def __init__(self, etat_civil, coordonnees):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

    def afficher_dossier(self):
        return f"État civil: {self.etat_civil}, Coordonnées: {self.coordonnees}"


class Professeur(Dossier):
    def __init__(self, etat_civil, coordonnees, matiere):
        super().__init__(etat_civil, coordonnees)
        self.matiere = matiere


class Eleve(Dossier):
    def __init__(self, etat_civil, coordonnees):
        super().__init__(etat_civil, coordonnees)


# Exemple d'utilisation
prof = Professeur("Mme Marie", "Femme", "Mathématiques")
classe = Classe(prof)

eleve1 = Eleve("Jean Dupuis", "Homme")
eleve2 = Eleve("Francois Curie", "Homme")
eleve3 = Eleve("Jean René", "Femme")

classe.ajouter_eleve(eleve1)
classe.ajouter_eleve(eleve2)
classe.ajouter_eleve(eleve3)

print(classe.afficher_classe())
