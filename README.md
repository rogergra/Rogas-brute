
# Rogas-brute

**Rogas-brute** est un outil de brute force conçu pour tester la sécurité des systèmes de connexion en ligne. Il utilise la bibliothèque Selenium pour effectuer des tentatives automatiques de connexion sur des pages web, en générant différentes combinaisons de noms d'utilisateur et de mots de passe. Cet outil est destiné à un usage éthique et à des fins de tests de sécurité pour identifier les failles de sécurité dans les réseaux Wi-Fi commerciaux gérés par MikroTik.

# Fonctionnalités

- **Génération de mots de passe** : Crée des combinaisons de mots de passe selon plusieurs formats (ex: `abc123`, `a1b2c3`).
- **Modes de bruteforce personnalisés** :
  - **Scénario 1** : Nom d'utilisateur = Mot de passe
  - **Scénario 2** : Nom d'utilisateur différent du mot de passe
- **Attente dynamique** : Utilise des attentes explicites pour détecter des changements dans l'interface de connexion.
- **Délai aléatoire** : Ajoute un délai aléatoire entre les tentatives pour minimiser les blocages par détection de tentatives automatiques.

# Prérequis

- **Python 3.7+**
- **Selenium** : Pour automatiser les tentatives de connexion.
- **Geckodriver** : Pour le navigateur Firefox. Assurez-vous d'installer geckodriver et de l’ajouter au PATH ou de spécifier son emplacement dans le script.

# Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/rogergra/rogas-brute.git
   cd rogas-brute
   ```

2. Installez les dépendances :
```bash
   pip install selenium
  ```

3. Assurez-vous que **geckodriver** est bien installé et accessible par le script.

# Utilisation

1. Exécutez le script dans un terminal :
 ```bash
   python rogas-brute.py
  ```

2. Fournissez les informations requises :
   - **URL** du site de connexion.
   - **Scénario** (1 pour nom d'utilisateur = mot de passe, 2 pour nom d'utilisateur ≠ mot de passe).
   - **Nombre de tentatives** maximal.

3. Le script tentera les combinaisons jusqu’à trouver une correspondance ou atteindre le nombre maximal de tentatives.

# Exemples

- Scénario 1 (Nom d'utilisateur = Mot de passe) :
  - Le script générera des combinaisons selon le format choisi (`abc123`, `a1b2c3`, etc.).
  
- Scénario 2 (Nom d'utilisateur ≠ Mot de passe) :
  - Génère des combinaisons distinctes pour le nom d'utilisateur et le mot de passe.

# Avertissement

**Rogas-brute** est destiné exclusivement à des fins de tests de sécurité légaux et autorisés. Toute utilisation de cet outil sans autorisation explicite du propriétaire du système pourrait constituer une violation des lois en vigueur. En téléchargeant et en utilisant **Rogas-brute**, vous vous engagez à respecter les lois et à utiliser cet outil uniquement pour des audits de sécurité éthiques.




contacter le developpeur email: Rogashack@gmail.com        · Rogastech2019@gmail.com
