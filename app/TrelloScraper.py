from ScraperImages import *



class TrelloScraper(Scraping):
    
    
    def ScrapingTrello(self):
        url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fb%252FurrViyEt%252Fdaily-cata%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
        self.driver.get(url)
        
        with open('app/config/login.yaml', 'r') as file:
            data = yaml.safe_load(file)

        for entry in data:
            if entry['service'] == 'trello':
                username = entry['username']
                password = entry['password']

        
        wait = WebDriverWait(self.driver, 30)
        inputUsername = wait.until(EC.presence_of_element_located((By.ID, "username")))
        inputUsername.send_keys(username)
        
        btnValider = wait.until(EC.presence_of_element_located((By.ID, "login-submit")))
        btnValider.click()
        time.sleep(6)
        
        
        inputPassword = wait.until(EC.presence_of_element_located((By.ID, "password")))
        inputPassword.send_keys(password)
        
        btnValider = wait.until(EC.presence_of_element_located((By.ID, "login-submit")))
        btnValider.click()
        time.sleep(10)
          # Récupérer le contenu HTML de la page actuelle
        html_content = self.driver.page_source

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Votre expression régulière pour rechercher une chaîne de caractères
        regex_pattern = rf'{re.escape("Reima")}'

        # Rechercher la chaîne de caractères en utilisant l'expression régulière
        matches = soup.find_all(text=re.compile(regex_pattern))

        time.sleep(5)
        # Si des correspondances sont trouvées, les afficher
        if matches:
            for match in matches:
                if "Images" in match:
                    return True
            # Si aucun match contenant "Images" n'est trouvé dans toutes les correspondances
            return False
        else:
            # Si aucune correspondance n'a été trouvée du tout
            return False
