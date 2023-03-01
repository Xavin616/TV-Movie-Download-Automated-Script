#!/usr/bin/env python

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

s = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=s, options=options)
params = {'behavior': 'allow', 'downloadPath': r'/home/xavin/Videos'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

def movies(query):
    driver.get(f"https://nkiri.com/?s={query}")
    found = driver.find_element_by_xpath('//h2[@class="search-entry-title entry-title"]//a')
    #found
    found.send_keys(Keys.ENTER)
    sleep(4)
    link = driver.find_element_by_xpath('//span[contains(text(), "Download Movie" )]')
    sleep(2)
    driver.execute_script("arguments[0].click();", link)
    k = driver.find_element_by_xpath("//button[@id='downloadbtn']")
    driver.execute_script("arguments[0].click();", k)

if __name__ == '__main__':
    print("Movie Downloader is loading....")
    search  = str(input("Name:\t"))
    movies(search)