from app.scraper.ScraperImages import *

class DownloaderScraper(Scraping):
    
    def scrapingDownloader(self):
        with open('app/config/downloaderData.yaml', 'r') as file:
            data = yaml.safe_load(file)
        
        for brand in data['downloader']:
            if self.nameBrand == brand:
                return True
        
        return False  # Return False only after all brands have been checked



