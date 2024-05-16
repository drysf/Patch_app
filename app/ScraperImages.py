import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import yaml


class Scraping:
    
    
    def __init__(self, nameBrand) -> None:
        self.nameBrand = nameBrand  
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.binary_location = '/home/drys/Documents/chrome-linux64/chrome'
        self.driver = webdriver.Chrome(options=self.chrome_options)
    

        
    
    def ScrapingFastTrack(self):
        url = "https://drive.google.com/drive/folders/1IEC1DSFn_HlZqSlP-CwP2R6FjjP_yeVK"
    
    
    def ScrapingUrlImages(self):
        url = "https://docs.google.com/spreadsheets/d/11Gn-Y6geGNTWNynZzqiDjHkvp7_b6LwtZ6njVCW0qnI/edit#gid=0"
        
    def ScrapingWms(self):
        url = "https://admin.wms.spacefoot.net/base/supplier/"
        
        
    def ScrapDownloader(self):
        pass        



