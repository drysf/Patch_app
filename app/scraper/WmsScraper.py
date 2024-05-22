from app.scraper.ScraperImages import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import yaml
import re
import time

class WmsScraper(Scraping):
    def WmsScraper(self):
        url = "https://admin.wms.spacefoot.net/base/supplier/"
        self.driver.get(url)

        with open('app/config/login.yaml', 'r') as file:
            data = yaml.safe_load(file)

        for entry in data:
            if entry['service'] == 'wms':
                username = entry['username']
                password = entry['password']

        wait = WebDriverWait(self.driver, 30)
        inputUsername = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
        inputUsername.send_keys(username)

        inputPassword = wait.until(EC.presence_of_element_located((By.ID, "id_password")))
        inputPassword.send_keys(password)

        inputValid = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input")))
        inputValid.click()

        searchBar = wait.until(EC.presence_of_element_located((By.ID, "searchbar")))
        searchBar.send_keys(self.nameBrand)

        validSearchBar = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div/div/div/form/div/input[2]")))
        validSearchBar.click()

        brandsEnum = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div/div/form/div/table/tbody/tr[1]/th/a")))
        brandsEnum[0].click()

        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        divs_with_class = soup.find_all('div', class_='field-webshop_url')
        regex_pattern = re.compile(r'http')
        matches = []

        for div in divs_with_class:
            div_text = div.get_text()
            if regex_pattern.search(div_text):
                clean_text = div_text.strip().replace('\n', '').replace('\xa0', ' ')
                matches.append(clean_text)

        time.sleep(10)

        if matches:
            return matches
        else:
            return False


