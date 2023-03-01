#!/usr/bin/env python
from driver import driver, By, Keys
from driver import args
from time import sleep
import sys


series_name = args.series
episodes = args.episodes
classic = args.classic
timeout = args.timeout

def series(query, start, stop, timeout, classic):
    driver.get(f"https://nkiri.com/?s={query}")
    sleep(3)
    xs = start
    found = driver.find_element(By.XPATH, "(//h2[@class='search-entry-title entry-title'])[1]/a")
    found.send_keys(Keys.ENTER)
    slist = driver.find_elements(By.XPATH, "//a[@role='button']")
    links = [a.get_attribute('href') for a in slist]
    for view in links[(start+1):(stop+2)]:
        # driver.eviewecute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[1])
        if classic:
            # print('Loading Legacy Download Program')
            driver.get(view)
            continue
        else:
            print(f"Downloading Episode: {xs}")
            driver.get(view)
            k = driver.find_element(By.XPATH, "//button[@id='downloadbtn']")
            driver.execute_script("arguments[0].click();", k)
            xs+=1
            continue
    sleep(timeout)
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])


if __name__ == '__main__':
    print('================================================')
    print("Nkiri Downloader is loading....")
    print(f"Series: {series_name.capitalize()}\nEpisodes: {episodes}")
    print('================================================')
    series(series_name, episodes[0], episodes[-1], timeout, classic)