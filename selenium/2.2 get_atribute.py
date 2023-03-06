import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By




browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    img = browser.find_element(By.ID,"treasure")
    x_atribbute = img.get_attribute("valuex")
    x = calc(x_atribbute)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(x)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

