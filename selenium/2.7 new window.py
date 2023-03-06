import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    button_1 = browser.find_element(By.TAG_NAME,"button")
    button_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    button_2 = browser.find_element(By.TAG_NAME,"button")
    button_2.click()

finally:
    time.sleep(15)
    browser.quit()
