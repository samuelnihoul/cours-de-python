import os
import shutil
from datetime import datetime
from ex4.main import lister_et_copier_fichier, compter_fichiers

class FileManager:
    def __init__(self, dossier_courant='.'):
        """
        Initialise le gestionnaire de fichiers
        :param dossier_courant: Le dossier sur lequel travailler (par défaut: dossier courant)
        """
        self.dossier_courant = dossier_courant

    def lister_et_copier(self):
        """
        Utilise la fonction de l'exercice 4 pour lister et copier un fichier
        """
        # Sauvegarder le dossier courant
        dossier_original = os.getcwd()
        
        # Changer vers le dossier spécifié
        os.chdir(self.dossier_courant)
        
        # Appeler la fonction de l'exercice 4
        lister_et_copier_fichier()
        
        # Revenir au dossier original
        os.chdir(dossier_original)

    def compter(self):
        """
        Utilise la fonction de l'exercice 4 pour compter les fichiers
        :return: Nombre de fichiers
        """
        return compter_fichiers(self.dossier_courant)

def main():
    # Créer une instance de FileManager
    fm = FileManager()

    # Question 1 : Lister et copier un fichier
    print("\n=== Question 1 : Lister et copier un fichier ===")
    fm.lister_et_copier()

    # Question 2 : Compter les fichiers
    print("\n=== Question 2 : Compter les fichiers ===")
    nombre = fm.compter()
    print(f"Nombre de fichiers dans le dossier courant : {nombre}")

if __name__ == "__main__":
    main()
