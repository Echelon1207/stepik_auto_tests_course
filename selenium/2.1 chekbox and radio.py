import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By




browser = webdriver.Chrome()
link = "https://suninjuly.github.io/math.html"

try:
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
finally:
    time.sleep(20)
    browser.quit()
