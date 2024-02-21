#this file is for initializations of the functions in functions.py

#importing required libraries
import os
import time

from selenium import webdriver 
from selenium.webdriver.common.by import By


import functions as func


dir = input("name of this directory? ")

yt_channel = input("Name of channel you wish to download? The @ of the channel without the @ sign: ")




parent_dir = "C:\\Users\muham\\Desktop\\personal_projects\\yt_downloader"
path = os.path.join(parent_dir, dir) #combine the parent dir and dir to create and save a new folder
#creating a webdriver instance

driver = func.create_webdriver()
#the link that we will be opening
driver.get(f'https://www.youtube.com/@{yt_channel}/videos')
func.scroll_to_bottom(driver)

#links finds all of the elements that have the correct href i.e the video link in its properties.
links = driver.find_elements(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.ytd-rich-grid-media')


#gettigng all the video links from the links we scraped
hrefs = [link.get_attribute('href') for link in links]

#filtering since elements are in the same class 
complete_hrefs = [href for href in hrefs if href is not None]

#starting the download process
for href in complete_hrefs:
    print(href)
    result = func.downloadVideo(href, path)
    print(f'{href}: {result}')

print('Total links:', len(complete_hrefs))

time.sleep(3)

driver.quit()