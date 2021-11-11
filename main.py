from time import sleep
from plyer import notification
from typing import ChainMap
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

s = Service(ChromeDriverManager().install())
options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-popup-blocking')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options, service=s)
params = {'behavior': 'allow', 'downloadPath': r'/home/xavin616/Videos'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

url = f"https://mobiletvshows.net/subfolder-Arcane.htm"

def notify():
    notification.notify(
        title = 'Tv Series Downloader Has Ended',
        message = 'Series has Downloaded, program has ended!',
        timeout = 5
    )
    sleep(5)

if __name__ == '__main__':
    driver.get(url)
    list = driver.find_elements_by_xpath('//small[contains(text(), "High MP4")]')
    number = int(len(list))
    for i in range(0, number):
        driver.get(url)
        list = driver.find_elements_by_xpath('//small[contains(text(), "High MP4")]')
        item = list[i]
        driver.execute_script("arguments[0].click();", item)
        #sleep(5)
        downlink = driver.find_element_by_id('dlink1')
        driver.execute_script("arguments[0].click();", downlink)
        sleep(5)
        link1 = driver.find_element_by_id('flink1')
        driver.execute_script("arguments[0].click();", link1)
        sleep(5)
    sleep(600)
    driver.close()
    print('Program has Ended')
    notify()