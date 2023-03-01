#!/usr/bin/env python

from driver import driver, By, Keys, Alert
from driver import args
from time import sleep

def notify():
    notification.notify(
        title = 'Tv Series Downloader Has Ended',
        message = 'Series has Downloaded, program has ended!',
        timeout = 5
    )

def main(url, start, stop,timeout):
    driver.get(url)
    Alert(driver).dismiss()
    eplist = driver.find_elements(By.XPATH, '//small[contains(text(), "High MP4")]')
    length = len(eplist)
    end = (length if stop > length else stop)
    print('================================================')
    for i in range(start-1, end):
        print("Downloading Episode: ", i+1)
        driver.get(url)
        xlist = driver.find_elements(By.XPATH, '//small[contains(text(), "High MP4")]')
        item = xlist[i]
        driver.execute_script("arguments[0].click();", item)
        downlink = driver.find_element(By.ID, 'dlink1')
        driver.execute_script("arguments[0].click();", downlink)
        link1 = driver.find_element(By.ID, 'flink1')
        driver.execute_script("arguments[0].click();", link1)
        #sleep(10)
    sleep(timeout)

if __name__ == '__main__':
    url = args.url
    start = args.episodes[0]
    stop = args.episodes[-1]
    time = args.timeout
    print('================================================')
    print(f'Url:{url}\nEpisodes: {start}-{stop}')
    main(url, start, stop, time)
    # notify()
