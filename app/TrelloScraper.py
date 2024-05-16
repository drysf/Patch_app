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
        time.sleep(1)
        
        
        inputPassword = wait.until(EC.presence_of_element_located((By.ID, "password")))
        inputPassword.send_keys(password)
        
        btnValider = wait.until(EC.presence_of_element_located((By.ID, "login-submit")))
        btnValider.click()
        
        
        time.sleep(3000)
        self.driver.quit()
        
scraper = TrelloScraper("nike")
scraper.ScrapingTrello()