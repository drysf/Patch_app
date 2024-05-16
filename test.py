import requests
from bs4 import BeautifulSoup

# URL de la page web
url = 'https://trello.com/b/urrViyEt/daily-cata'

# Récupérer le contenu HTML de la page
response = requests.get(url)
html_content = response.text

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver la balise <div> spécifique (par exemple, avec une classe CSS)
div = soup.find('div', class_='nom_de_classe_css')


# Vérifier si la balise <div> a été trouvée
if div:
    # Rechercher la chaîne de caractères dans la balise <div>
    string_to_find = 'votre_string_a_rechercher'
    if string_to_find in div.text:
        print(f"La chaîne '{string_to_find}' a été trouvée dans la balise <div>.")
    else:
        print(f"La chaîne '{string_to_find}' n'a pas été trouvée dans la balise <div>.")
else:
    print("La balise <div> spécifique n'a pas été trouvée sur la page.")
