from pandas_utils import (
    read_file,
    filter_boolean_yes,
    filter_url_contains_reddit,
    calculate_percentage,
    save_filtered_dataframes
)

def main():
    # Chemin vers le fichier CSV
    file_path = 'ex7.csv'  # Remplacez par le chemin de votre fichier
    
    try:
        # Lecture du fichier
        df = read_file(file_path)
        
        # Filtrage des données
        boolean_yes_df = filter_boolean_yes(df)
        url_reddit_df = filter_url_contains_reddit(df)
        
        # Calcul des pourcentages
        percentage_boolean, percentage_reddit = calculate_percentage(df, boolean_yes_df, url_reddit_df)
        
        # Affichage des résultats
        print(f"Pourcentage de lignes avec 'boolean' = 'Yes': {percentage_boolean:.2f}%")
        print(f"Pourcentage de lignes contenant 'reddit' dans l'URL: {percentage_reddit:.2f}%")
        
        # Sauvegarde des DataFrames filtrés
        save_filtered_dataframes(df, boolean_yes_df, url_reddit_df, 'filtered_data')
        print("Les fichiers filtrés ont été sauvegardés dans le dossier 'filtered_data'")
        
    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    main()
