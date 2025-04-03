import subprocess
from fabric import Connection

def list_local_interfaces():
    """Liste les interfaces réseau du système local en utilisant subprocess"""
    try:
        # Pour Windows
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        print("Interfaces réseau locales (Windows):")
        print(result.stdout)
    except Exception as e:
        print(f"Erreur lors de la récupération des interfaces locales: {e}")

def list_remote_interfaces(host, user, password):
    """Liste les interfaces réseau d'une machine distante en utilisant fabric"""
    try:
        # Connexion à la machine distante
        with Connection(host=host, user=user, connect_kwargs={"password": password}) as conn:
            # Pour Linux/Unix
            result = conn.run('ifconfig', hide=True)
            print(f"\nInterfaces réseau distantes ({host}):")
            print(result.stdout)
    except Exception as e:
        print(f"Erreur lors de la récupération des interfaces distantes: {e}")

if __name__ == "__main__":
    # Liste les interfaces locales
    list_local_interfaces()
    
    # Exemple d'utilisation pour une machine distante
    # Remplacez ces valeurs par vos informations de connexion
    remote_host = "localhost"
    remote_user = "samuelnihoul"
    remote_password = ""
    
    # Décommentez la ligne suivante pour tester la connexion distante
    list_remote_interfaces(remote_host, remote_user, remote_password)
