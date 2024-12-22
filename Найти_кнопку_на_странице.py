import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

# input = browser.find_element(By.CSS_SELECTOR, "input[name=first_name]")
# input.click()
# input.send_keys("Floyd")
# input1 = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
# input1.click()
# input1.send_keys("Russia")
button = browser.find_element(By.ID, "submit_button")
button.click()
time.sleep(15)
browser.quit()