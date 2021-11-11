from time import sleep
from typing import List
from webbrowser import open as wb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

s = Service(ChromeDriverManager().install())
options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=s, options=options)
params = {'behavior': 'allow', 'downloadPath': r'/home/xavin616/Videos'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

#url = f"https://nkiri.com/while-you-were-sleeping-korean-drama/"

def search(query):
    driver.get(f"https://nkiri.com/?s={query}")
    found = driver.find_element_by_xpath('//h2[@class="search-entry-title entry-title"]//a')
    #found
    found.send_keys(Keys.ENTER)
    print(found.text)

def series(query, episode):
    driver.get(f"https://nkiri.com/?s={query}")
    found = driver.find_element_by_xpath('//h2[@class="search-entry-title entry-title"]//a')
    #found
    found.send_keys(Keys.ENTER)
    sleep(4)
    list = driver.find_elements_by_xpath('//span[contains(text(), "Download Episode" )]')
    num = len(list)
    for i in range((episode-1), num):
        sleep(2)
        driver.execute_script("arguments[0].click();", list[i])
        sleep(4)

def movies(query):
    driver.get(f"https://nkiri.com/?s={query}")
    found = driver.find_element_by_xpath('//h2[@class="search-entry-title entry-title"]//a')
    #found
    found.send_keys(Keys.ENTER)
    print(found.text)
    sleep(4)
    link = driver.find_element_by_xpath('//span[contains(text(), "Download Movie" )]')
    sleep(2)
    driver.execute_script("arguments[0].click();", link)
    sleep(300)

if __name__ == '__main__':
    print("Nkiri Downloader is loading....")
    search  = str(input("Name:\t"))
    media = str(input("Media ('movie'/ 'tv'):\t"))
    episode = int(input("If series, which episode should I start from (a number):\t"))

    if 'movie' in media:
        movies(search)
    else:
        series(search, episode)
    