import os
import time

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import pytube as pt
from pytube.exceptions import AgeRestrictedError

#allows us to scroll t the end of the ppage
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        time.sleep(2)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break #we're at the bottom
        last_height = new_height



#our yt video downloader function
def downloadVideo(link, path):
    try:
        video = pt.YouTube(link)
        #you can set the res  to whatever u want
        video.streams.filter(res='720p').first().download(path) 
        return "Downloaded"
    except AgeRestrictedError as e:
        print(f'Error: Age restricted video {link}, skipping ....')
        return "Skipped"
    except Exception as e:
        print(f'Error for video {link} : {e}')
        return "Skipped"  

def create_webdriver():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("start-maximized")  
    chrome_options.add_argument("disable-infobars")  
    chrome_options.add_argument("--disable-extensions")  


    driver = webdriver.Chrome(options=chrome_options)
    return driver


