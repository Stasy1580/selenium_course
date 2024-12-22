from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
              
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME,"last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")


# SelectorsHub extention for Chrome - nice helper to see exacts XPath selectors
# https://stackoverflow.com/questions/73843069/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath
# https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath

#	all these variants works fine:
#    button = browser.find_element(By.XPATH, "/html/body/div/form//button[@type='submit']")
#    button = browser.find_element(By.XPATH, "//button[@type='submit']")
#    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button = browser.find_element(By.XPATH, "/html/body/div/form//button[text()=\"Submit\"]")
    button.click()
# or (equal)
#    button = browser.find_element(By.XPATH, "/html/body/div/form//button[text()=\"Submit\"]").click()



#    doesn't work:
#    button = browser.find_element(By.XPath_SELECTOR, "/html/body/div/form/div[6]/button[3]")
#    button = browser.find_element(By.XPath_SELECTOR, "/html/body/div/form//button[text()=\"Submit\"]")
#    button.click()

finally:
    
    time.sleep(30)
    browser.quit()
