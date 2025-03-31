from ip_address import detecter_et_valider_ip
def valider_dict_ip(dict_ip):
    resultats = []
    try:
        for host, ip in dict_ip.items():
            try:
                ip = str(ip).strip()
                if ip:
                    resultat = detecter_et_valider_ip(ip)
                    resultats.append({
                        'host': host,
                        'adresse': ip,
                        'type': resultat,
                        'valide': resultat is not None
                    })
            except AttributeError as e:
                print(f"Erreur avec l'adresse IP de {host}: {e}")
            except Exception as e:
                print(f"Erreur inattendue pour {host}: {e}")
    except TypeError as e:
        print(f"Erreur: Le paramètre d'entrée doit être un dictionnaire. {e}")
    except Exception as e:
        print(f"Erreur inattendue lors du traitement: {e}")
    
    return resultats

# Test avec simulation d'erreurs
test_dict = {
    'serveur1': '192.168.1.1',
    'serveur2': None,  # Simuler une erreur
    'serveur3': 12345,  # Simuler une erreur de type
    'serveur4': '2001:db8::8a2e:370:7334'
} 