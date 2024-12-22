from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = " https://suninjuly.github.io/selects2.html"


def calc(x,y):
    return int(x)+int(y)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = calc(x, y)
    z_str = str(z)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z_str)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()