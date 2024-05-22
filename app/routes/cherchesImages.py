from flask import render_template, request
from app.scraper.DownloaderScraper import DownloaderScraper
from app.scraper.FastTrackScraper import FastTrackScraper
from app.scraper.TrelloScraper import TrelloScraper
from app.scraper.UrlImagesScraper import UrlImagesScraper
from app.scraper.WmsScraper import WmsScraper
from app import app



@app.route('/Cherche_les_images', methods=['GET', 'POST'])
def Cherche_les_images():
    results = {}
    nom_marque = None
    if request.method == "POST":
        nom_marque = request.form['nom_marque']
        
        downloader_scraper = DownloaderScraper(nom_marque)
        fast_track_scraper = FastTrackScraper(nom_marque)
        trello_scraper = TrelloScraper(nom_marque)
        url_images_scraper = UrlImagesScraper(nom_marque)
        wms_scraper = WmsScraper(nom_marque)

        results['downloader'] = downloader_scraper.scrapingDownloader()
        results['fast_track'] = fast_track_scraper.ScrapingFastTrack()
        # results['trello'] = trello_scraper.ScrapingTrello()
        results['url_images'] = url_images_scraper.ScrapingUrlImages()
        results['wms'] = wms_scraper.WmsScraper()
    
    return render_template('chercherDesImages.html', results=results, nom_marque=nom_marque)
