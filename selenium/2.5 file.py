import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    inputs = browser.find_elements(By.CSS_SELECTOR,"input[type='text']")
    for i in inputs:
        i.send_keys('t')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir,'test')
    element = browser.find_element(By.ID,"file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button.click()

finally:
    time.sleep(15)
    browser.quit()



