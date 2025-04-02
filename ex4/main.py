import os
import shutil
from datetime import datetime
import sys

def lister_et_copier_fichier():
    """Liste le contenu du dossier et crée une copie d'un fichier avec la date et l'heure"""
    # Lister le contenu du dossier
    fichiers = os.listdir('.')
    print("Contenu du dossier :")
    for fichier in fichiers:
        print(f"- {fichier}")
    
    # Demander à l'utilisateur quel fichier copier
    fichier_a_copier = input("\nQuel fichier voulez-vous copier ? ")
    
    if os.path.isfile(fichier_a_copier):
        # Créer le nom du fichier avec la date et l'heure
        date_heure = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_copie = f"{os.path.splitext(fichier_a_copier)[0]}_{date_heure}{os.path.splitext(fichier_a_copier)[1]}"
        
        # Copier le fichier
        shutil.copy2(fichier_a_copier, nom_copie)
        print(f"\nCopie créée avec succès : {nom_copie}")
    else:
        print("Le fichier spécifié n'existe pas.")

def compter_fichiers(dossier='.'):
    """Compte le nombre de fichiers (pas les dossiers) dans le dossier spécifié"""
    nombre_fichiers = 0
    for element in os.listdir(dossier):
        if os.path.isfile(os.path.join(dossier, element)):
            nombre_fichiers += 1
    return nombre_fichiers

def main():
    # Question 1 : Lister et copier un fichier
    print("\n=== Question 1 : Lister et copier un fichier ===")
    lister_et_copier_fichier()
    
    # Question 2 : Compter les fichiers
    print("\n=== Question 2 : Compter les fichiers ===")
    nombre = compter_fichiers()
    print(f"Nombre de fichiers dans le dossier courant : {nombre}")
    
    # Question 3 : Compter les fichiers dans un dossier spécifié en argument
    print("\n=== Question 3 : Compter les fichiers dans un dossier spécifié ===")
    if len(sys.argv) > 1:
        dossier = sys.argv[1]
        if os.path.isdir(dossier):
            nombre = compter_fichiers(dossier)
            print(f"Nombre de fichiers dans le dossier {dossier} : {nombre}")
        else:
            print(f"Le dossier {dossier} n'existe pas.")
    else:
        print("Aucun dossier spécifié en argument. Utilisation du dossier courant.")
        nombre = compter_fichiers()
        print(f"Nombre de fichiers dans le dossier courant : {nombre}")

if __name__ == "__main__":
    main()
