from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    #def fill_regisration_form (link):


    def test_registration1(self):
        self.browser = webdriver.Chrome()
        self.browser.get(link1)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "input:required.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "input:required.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("a@mail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Element not found")

        self.browser.quit()

    def test_registration2(self):
        self.browser = webdriver.Chrome()
        self.browser.get(link2)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "input:required.first")
        input1.send_keys("Maria")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "input:required.second")
        input2.send_keys("Petrova")
        input3 = self.browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys("aaa@mail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Element not found")

        self.browser.quit()

if __name__ == "__main__":
    unittest.main()