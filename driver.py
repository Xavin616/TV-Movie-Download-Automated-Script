#!/usr/bin/env python

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--series', action='store', type=str)
parser.add_argument('-e', '--episodes', action='store', type=int, nargs='+')
parser.add_argument('-u', '--url', action='store', type=str)
parser.add_argument('-c', '--classic', type=bool, default=False, action='store')
parser.add_argument('-t', '--timeout', type=int, action='store', default=300)

args = parser.parse_args()

s = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--log-level=3")
#options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=s, options=options)
params = {'behavior': 'allow', 'downloadPath': r'/home/xavin/Videos'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

