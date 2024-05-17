from ScraperImages import *

class DownloaderScraper(Scraping):
    
    def scrapingDownloader(self):
        with open('app/config/downloaderData.yaml', 'r') as file:
            data = yaml.safe_load(file)
        
        for brand in data['downloader']:
            if "click" == brand:
                return True
        
        return False  # Return False only after all brands have been checked

# Create an instance of DownloaderScraper with "nike"
nike = DownloaderScraper("nike")

# Call the scrapingDownloader method and print the result
print(nike.scrapingDownloader())
