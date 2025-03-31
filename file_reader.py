from text_processor import remplacer_lettres
def lire_fichier_vers_dict(chemin_fichier):
    """
    Lit un fichier et stocke son contenu dans un dictionnaire
    """
    contenu_dict = {}
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as file:
            for num_ligne, ligne in enumerate(file, 1):
                contenu_dict[num_ligne] = ligne.rstrip('\n')
        return contenu_dict
    except FileNotFoundError:
        print(f"Erreur: Le fichier {chemin_fichier} n'existe pas")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    return {}

def afficher_contenu_dict(dictionnaire):
    """
    Affiche le contenu du dictionnaire selon le format demandé
    """
    try:
        for num_ligne, contenu in dictionnaire.items():
            print(f"Ligne numéro {num_ligne} : {len(contenu)} caractères → \"{contenu}\"")
    except Exception as e:
        print(f"Erreur lors de l'affichage: {e}")

# Programme principal pour tester
def main():
    # Test de remplacement de lettres
    chemin_fichier = "test.txt"
    
    # Créer un fichier de test
    try:
        with open(chemin_fichier, 'w') as f:
            f.write("Voici la première ligne\nDeuxième ligne de test\nTroisième ligne!")
    except Exception as e:
        print(f"Erreur lors de la création du fichier de test: {e}")
        return

    # Test des différentes fonctionnalités
    print("1. Contenu original du fichier:")
    dict_original = lire_fichier_vers_dict(chemin_fichier)
    afficher_contenu_dict(dict_original)

    print("\n2. Remplacement des lettres:")
    remplacer_lettres(chemin_fichier, ['a', 'e', 'i'])

    print("\n3. Contenu après remplacement:")
    dict_modifie = lire_fichier_vers_dict(chemin_fichier)
    afficher_contenu_dict(dict_modifie)

if __name__ == "__main__":
    main() 