import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Rundeck():
    
    def EnvoiRundeck(patchName, resultFile):  
        
        resultFile = f"/home/drys/Public/imports-magmi/data/{resultFile}"

        chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.binary_location = '/home/drys/Documents/chrome-linux64/chrome'
        driver = webdriver.Chrome(options=chrome_options)
        
        id = "drys.ferhi"
        password = "5fva4ohe!Tj!oc2oZY563ANR3pGh9t"

        url = "https://rundeck.spacefoot.net/project/Ebiz/job/show/1d93e5cc-098e-494c-8f73-267e8a0f8b08"

        driver.get(url)
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login")))
        
        inputLogin = driver.find_element(By.ID, "login")
        inputLogin.send_keys(id)

        inputPassword = driver.find_element(By.ID, "password")
        inputPassword.send_keys(password)
        
        btnLogin = driver.find_element(By.ID, "btn-login")
        btnLogin.click()
        
        time.sleep(0.1)
        
        inputPatch = driver.find_element(By.XPATH, "/html/body/section[1]/section[2]/div[2]/div/div/div[1]/div/div/div/div[1]/form/div/div/section[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/input")
        inputPatch.send_keys(patchName)
        
        time.sleep(0.1)
        
        inputExport = driver.find_element(By.XPATH, "/html/body/section[1]/section[2]/div[2]/div/div/div[1]/div/div/div/div[1]/form/div/div/section[2]/div[2]/div/div[3]/div/div[1]/div[1]/div/input")
        inputExport.send_keys(resultFile)
        
        btnEnvoiRundeck = driver.find_element(By.ID, "execFormRunButton")
        btnEnvoiRundeck.click()
        
        time.sleep(2)
        
        def is_element_present():
            try:
                driver.find_element(By.ID, "progressContainer2")
                return True
            except:
                return False

        # Attendre jusqu'à ce que l'élément ne soit plus présent dans le DOM
        while is_element_present():
            time.sleep(3)  # 
            
            
        time.sleep(10)
        driver.quit()

Rundeck.EnvoiRundeck(patchName="salut", resultFile="export_464.csv")
