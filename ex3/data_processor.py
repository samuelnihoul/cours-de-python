import requests
import csv
import json
from typing import Dict, Any, List
import os
from ex1.ip_address import ask_for_a_dict_of_addresses

def get_api_data(url: str, method: str = 'GET', data: Dict = None) -> Dict[str, Any]:
    """
    Effectue une requête à une API et retourne les données
    Gère les erreurs 4xx
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        else:
            raise ValueError("Méthode HTTP non supportée")

        # Vérifier si la requête a réussi
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as e:
        if 400 <= e.response.status_code < 500:
            print(f"Erreur client (4xx): {e.response.status_code}")
            print(f"Message d'erreur: {e.response.text}")
        else:
            print(f"Erreur HTTP: {e.response.status_code}")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return {}

def process_csv(input_file: str, output_file: str, processing_func) -> None:
    """
    Importe un fichier CSV, modifie son contenu et sauvegarde dans un nouveau fichier
    """
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Le fichier {input_file} n'existe pas")

        # Lire le fichier CSV d'origine
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            rows = list(reader)
            
            # Traiter chaque ligne
            processed_rows = [processing_func(row) for row in rows]

        # Sauvegarder dans un nouveau fichier
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            if processed_rows:
                writer = csv.DictWriter(outfile, fieldnames=processed_rows[0].keys())
                writer.writeheader()
                writer.writerows(processed_rows)

        print(f"Traitement CSV terminé. Résultat sauvegardé dans {output_file}")

    except Exception as e:
        print(f"Erreur lors du traitement du CSV: {e}")

def export_to_json(data: Dict[str, Any], output_file: str) -> None:
    """
    Exporte des données dans un fichier JSON
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Données exportées avec succès dans {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'export JSON: {e}")

def export_to_csv(data: dict, output_file: str) -> None:
    """
    Exporte des données dans un fichier CSV avec des en-têtes
    """
    # try:
    print(data)
    print(type(data))
    if not data:
        raise ValueError("Aucune donnée à exporter")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=('serveur','hôte'))
        writer.writeheader()
        writer.writerows(data)
    print(f"Données exportées avec succès dans {output_file}")
    # except Exception as e:
        # print(f"Erreur lors de l'export CSV: {e}")
def process_row(row):
    # Exemple de modification: convertir les valeurs en majuscules
    return {k: v.upper() for k, v in row.items()}
# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple d'appel API
    api_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    api_data = get_api_data(api_url)
    process_csv("input.csv", "output.csv", process_row)
    user_input=ask_for_a_dict_of_addresses()
    export_to_csv(user_input, "output3.csv")
    export_to_json(user_input,"output2.json")
    