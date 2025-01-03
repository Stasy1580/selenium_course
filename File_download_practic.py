from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "form > div :nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("a@mail.ru")

    input4 = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Test.txt')
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except NoSuchElementException:
    print("Element not found")

except InvalidArgumentException as error:
    print ("invalid argument: " + error.msg)

except AssertionError:
    print("shinima!")

finally:

    time.sleep(10)

    browser.quit()