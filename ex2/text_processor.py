import fileinput
import os

def remplacer_lettres(chemin_fichier, lettres_a_remplacer=['a', 'e', 'i']):
    """
    Remplace les lettres spécifiées par 'x' dans un fichier
    """
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(chemin_fichier):
            raise FileNotFoundError(f"Le fichier {chemin_fichier} n'existe pas")

        # Créer un fichier de sauvegarde
        fichier_backup = chemin_fichier + '.bak'
        with open(chemin_fichier, 'r') as source:
            with open(fichier_backup, 'w') as backup:
                backup.write(source.read())

        # Remplacer les lettres
        with fileinput.FileInput(chemin_fichier, inplace=True, backup=None) as file:
            for ligne in file:
                for lettre in lettres_a_remplacer:
                    ligne = ligne.replace(lettre, 'x')
                print(ligne, end='')  # print écrit dans le fichier en mode inplace

        print(f"Remplacement effectué avec succès dans {chemin_fichier}")
        
    except PermissionError:
        print("Erreur: Permissions insuffisantes pour accéder au fichier")
    except UnicodeDecodeError:
        print("Erreur: Le fichier n'est pas encodé en texte lisible")
    except Exception as e:
        print(f"Erreur inattendue: {e}") 