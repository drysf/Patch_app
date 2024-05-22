from app.scraper.ScraperImages import *

class FastTrackScraper(Scraping):
    
    
    def ScrapingFastTrack(self):
        url = "https://drive.google.com/drive/folders/1IEC1DSFn_HlZqSlP-CwP2R6FjjP_yeVK"
        self.driver.get(url)
        
        
        html_content = self.driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        # Votre expression régulière pour rechercher une chaîne de caractères
        regex_pattern = rf'{re.escape(self.nameBrand)}'
        matches = soup.find_all(text=re.compile(regex_pattern))

        time.sleep(5)
        if matches:
            return True
        else:
            return False
        
    