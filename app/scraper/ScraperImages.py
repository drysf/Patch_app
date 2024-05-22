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
import re
from bs4 import BeautifulSoup


class Scraping:
    
    
    def __init__(self, nameBrand) -> None:
        self.nameBrand = nameBrand  
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless=new")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.binary_location = '/home/drys/Documents/chrome-linux64/chrome'
        self.driver = webdriver.Chrome(options=self.chrome_options)   



