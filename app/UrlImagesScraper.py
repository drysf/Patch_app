from ScraperImages import *

class UrlImagesScraper(Scraping):
    
    
    def ScrapingUrlImages(self):
        
        url = "https://docs.google.com/spreadsheets/d/11Gn-Y6geGNTWNynZzqiDjHkvp7_b6LwtZ6njVCW0qnI/edit#gid=0"
    
        self.driver.get(url)
        
        
        html_content = self.driver.page_source

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Votre expression régulière pour rechercher une chaîne de caractères
        regex_pattern = rf'{re.escape("ta grand mere la grosse pute pk ca fonctionne pas")}'

        # Rechercher la chaîne de caractères en utilisant l'expression régulière
        matches = soup.find_all(text=re.compile(regex_pattern))

        time.sleep(5)
        # Si des correspondances sont trouvées, les afficher
        if matches:
            return True
        else:
            # Si aucune correspondance n'a été trouvée du tout
            return False
        
        
        time.sleep(200)
        
nike = UrlImagesScraper("nike")

print(nike.ScrapingUrlImages())