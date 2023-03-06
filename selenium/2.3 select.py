import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    num_1 = browser.find_element(By.ID,"num1")
    one = num_1.text
    num_2 = browser.find_element(By.ID,"num2")
    two = num_2.text
    answer = int(one) + int(two)
    answer_str = str(answer)
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(answer_str)
    button = browser.find_element(By.TAG_NAME,"button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
