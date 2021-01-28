import time
from selenium import webdriver
def playyt(url):
    try:
        browser=webdriver.Firefox()
    except:
        print('You need Firefox and geckodriver installed')
    browser.get(url)
    button=browser.find_element_by_class_name('ytp-play-button')
    fullscreen=browser.find_element_by_class_name('ytp-fullscreen-button')
    button.click()
    #fullscreen.click()
