import socket
import sys
from datetime import datetime

def banner():
    print("-" * 50)
    print("🚀  PYSCANNER - NETWORK PORT SCANNER")
    print("    Bachelor Cyber Security Project")
    print("-" * 50)

def scan_target(target, ports):
    print(f"\n[*] Démarrage du scan sur : {target}")
    print(f"[*] Scan commencé à : {str(datetime.now())}")
    print("-" * 50)

    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                service_name = get_service_name(port)
                print(f"[+] Port {port} \t: OUVERT ({service_name})")

            s.close()

    except KeyboardInterrupt:
        print("\n[!] Arrêt du scan.")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Impossible de résoudre le nom de domaine.")
        sys.exit()
    except socket.error:
        print("\n[!] Impossible de se connecter au serveur.")
        sys.exit()

    print("-" * 50)
    print("[*] Scan terminé.")

def get_service_name(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        135: "RPC",
        139: "NetBIOS",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt"
    }
    return services.get(port, "Inconnu")

if __name__ == "__main__":
    banner()

    target_input = input("Entrez l'IP ou le domaine à scanner (ex: scanme.nmap.org) : ")

    try:
        target_ip = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("Erreur: Domaine invalide.")
        sys.exit()

    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]

    scan_target(target_ip, common_ports)