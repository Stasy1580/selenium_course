from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "form div.form-check:nth-child(4) input")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # if (button.get_attribute("class").find("btn-default")!=-1):
    #     button.click()
    # if (option2.get_attribute("type")=="radio"):
    #     option1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(20)
    browser.quit()
