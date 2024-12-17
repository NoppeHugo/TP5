class Email:
    def __init__(self, expediteur, destinataire, titre=None, texte=None, fichiers_joints=None):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.titre = titre
        self.texte = texte
        self.fichiers_joints = fichiers_joints if fichiers_joints else []

    def ajouter_fichier_joint(self, fichier):
        self.fichiers_joints.append(fichier)
        
class FichierJoint:
    def __init__(self, nom, contenu):
        self.nom = nom
        self.contenu = contenu
