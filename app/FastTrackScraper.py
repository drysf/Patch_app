from ScraperImages import *

class FastTrackScraper(Scraping):
    
    
    def ScrapingFastTrack(self):
        url = "https://drive.google.com/drive/folders/1IEC1DSFn_HlZqSlP-CwP2R6FjjP_yeVK"
        self.driver.get(url)
        
        
        html_content = self.driver.page_source

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Votre expression régulière pour rechercher une chaîne de caractères
        regex_pattern = rf'{re.escape("ADEVA")}'

        # Rechercher la chaîne de caractères en utilisant l'expression régulière
        matches = soup.find_all(text=re.compile(regex_pattern))

        time.sleep(5)
        # Si des correspondances sont trouvées, les afficher
        if matches:
            return True
        else:
            # Si aucune correspondance n'a été trouvée du tout
            return False
        
nike = FastTrackScraper("nike")
print(nike.ScrapingFastTrack())
    