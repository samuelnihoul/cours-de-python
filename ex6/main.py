import os
import json
import platform
import psutil
import datetime

def get_system_info():
    """
    Récupère les informations système et les retourne sous forme de dictionnaire
    """
    system_info = {
        "system": {
            "os": platform.system(),
            "os_version": platform.version(),
            "os_release": platform.release(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "hostname": platform.node(),
            "python_version": platform.python_version()
        },
        "hardware": {
            "cpu_count": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            "memory_total": psutil.virtual_memory().total,
            "memory_available": psutil.virtual_memory().available,
            "disk_usage": psutil.disk_usage('/')._asdict()
        },
        "timestamp": datetime.datetime.now().isoformat()
    }
    return system_info

def export_system_info(file_path="system_info.json"):
    """
    Exporte les informations système dans un fichier JSON
    """
    system_info = get_system_info()
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(system_info, f, indent=4)
    return file_path

def get_processes_info():
    """
    Récupère les informations de tous les processus
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'status', 'create_time']):
        try:
            process_info = proc.info
            process_info['create_time'] = datetime.datetime.fromtimestamp(process_info['create_time']).isoformat() if process_info['create_time'] else None
            processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def export_processes_info(file_path="processes_info.json"):
    """
    Exporte les informations des processus dans un fichier JSON
    """
    processes = get_processes_info()
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(processes, f, indent=4)
    return file_path

def get_high_memory_processes(threshold=2.0):
    """
    Retourne les processus qui consomment plus de threshold% de RAM
    """
    high_memory_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            process_info = proc.info
            if process_info['memory_percent'] > threshold:
                high_memory_processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return high_memory_processes

def main():
    # Question 1 : Exporter les informations système
    print("\n=== Question 1 : Export des informations système ===")
    system_info_file = export_system_info()
    print(f"Informations système exportées dans : {system_info_file}")

    # Question 2 : Exporter les informations des processus
    print("\n=== Question 2 : Export des informations des processus ===")
    processes_file = export_processes_info()
    print(f"Informations des processus exportées dans : {processes_file}")

    # Question 3 : Afficher les processus consommant plus de 2% de RAM
    print("\n=== Question 3 : Processus consommant plus de 2% de RAM ===")
    high_memory_processes = get_high_memory_processes()
    if high_memory_processes:
        print("\nProcessus consommant plus de 2% de RAM :")
        for proc in sorted(high_memory_processes, key=lambda x: x['memory_percent'], reverse=True):
            print(f"- {proc['name']} (PID: {proc['pid']}) : {proc['memory_percent']:.1f}%")
    else:
        print("Aucun processus ne consomme plus de 2% de RAM.")

if __name__ == "__main__":
    main()
