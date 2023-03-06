import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'https://ya.ru/?nr=1&redirect_ts=1677827014.85931&sso_failed=blocked&uuid=a3a51c6c-eb94-4023-bdb6-98d8e8bd0da4'


try:
    browser.get(link)
    search = browser.find_element(By.ID,"text")
    search.send_keys("рыба")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()