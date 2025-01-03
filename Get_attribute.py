from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")
    x = int(x_value)
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
