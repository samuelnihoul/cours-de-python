def valider_ipv4(ip):
    # Diviser l'adresse IP en octets
    octets = ip.split('.')
    
    # Vérifier s'il y a exactement 4 octets
    if len(octets) != 4:
        return False
    
    # Vérifier chaque octet
    for octet in octets:
        try:
            # Convertir l'octet en entier
            num = int(octet)
            # Vérifier si l'octet est entre 0 et 255
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True

def valider_ipv6(ip):
    # Diviser l'adresse IP en groupes
    groupes = ip.split(':')
    
    # Vérifier le nombre de groupes (doit être 8)
    if len(groupes) != 8:
        # Vérifier s'il y a une notation abrégée avec ::
        if '::' in ip:
            groupes = ip.split('::')
            if len(groupes) != 2 or ip.count('::') > 1:
                return False
        else:
            return False
    
    # Vérifier chaque groupe
    for groupe in groupes:
        # Ignorer les groupes vides dans le cas d'une notation ::
        if groupe == '':
            continue
            
        # Vérifier la longueur du groupe
        if len(groupe) > 4:
            return False
            
        # Vérifier si les caractères sont valides
        try:
            # Convertir le groupe en entier hexadécimal
            int(groupe, 16)
        except ValueError:
            return False
    
    return True

def detecter_et_valider_ip(ip):
    # Détecter si c'est une IPv4 (contient des points) ou IPv6 (contient des :)
    if '.' in ip:
        # Potentiellement IPv4
        if valider_ipv4(ip):
            return "IPv4"
        else:
            return None
    elif ':' in ip:
        # Potentiellement IPv6
        if valider_ipv6(ip):
            return "IPv6"
        else:
            return None
    else:
        return None

def valider_dict_ip(dict_ip):
    resultats = []
    for host, ip in dict_ip.items():
        ip = str(ip).strip()  # Convertir en string et enlever les espaces
        if ip:  # Ignorer les valeurs vides
            resultat = detecter_et_valider_ip(ip)
            resultats.append({
                'host': host,
                'adresse': ip,
                'type': resultat,
                'valide': resultat is not None
            })
    return resultats


def ask_for_a_dict_of_addresses()->dict:
    dict_adresses = {}
    while True:
        ligne = input()
        if ligne == "":  # Double Entrée pour terminer
            break
        try:
            host, ip = ligne.split(None, 1)  # Séparer en deux parties (host et IP)
            dict_adresses[host] = ip
        except ValueError:
            print("Format incorrect. Utilisez: 'host adresse_ip'")
            continue
    return(dict_adresses)
if __name__ == '__main__':
    # Valider toutes les adresses
    resultats = valider_dict_ip(ask_for_a_dict_of_addresses())

    # Afficher les résultats
    print("\nRésultats de la validation :")
    print("-" * 60)
    print(f"{'Hôte':<20} {'Adresse IP':<35} {'Statut'}")
    print("-" * 60)
    for res in resultats:
        if res['valide']:
            print(f"{res['host']:<20} {res['adresse']:<35} ✓ {res['type']}")
        else:
            print(f"{res['host']:<20} {res['adresse']:<35} ✗ Invalide") 