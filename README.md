# 🚀 PyScanner - Network Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Cybersecurity](https://img.shields.io/badge/Focus-Network%20Security-red)
![License](https://img.shields.io/badge/License-MIT-green)

**PyScanner** est un outil de reconnaissance réseau léger développé en Python. Il permet de scanner une cible (IP ou domaine) pour identifier les ports ouverts et les services associés via des connexions TCP.

> 🎓 *Ce projet a été réalisé dans le cadre de mon Bachelor en Cybersécurité pour approfondir ma compréhension du modèle OSI (Couche Transport) et des sockets.*

## ✨ Fonctionnalités

* **Résolution DNS automatique :** Convertit les noms de domaine (ex: `scanme.nmap.org`) en adresses IP.
* **TCP Connect Scan :** Établit une connexion complète (3-way handshake) pour vérifier l'état du port.
* **Identification de Service :** Associe les ports ouverts à leurs services standards (80 -> HTTP, 22 -> SSH, etc.).
* **Zéro Dépendance :** Utilise uniquement les librairies natives de Python (`socket`, `sys`), aucune installation complexe requise.

## 🛠️ Installation & Utilisation

Ce script fonctionne sur Windows, Linux et macOS sans configuration particulière.

### 1. Cloner le projet
```bash
git clone [https://github.com/TON-PSEUDO/PyScanner.git](https://github.com/TON-PSEUDO/PyScanner.git)
cd PyScanner
