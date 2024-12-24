from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    def fill_registration_form (self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)

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

    def test_registration1(self):
        self.fill_registration_form (link1)

    def test_registration2(self):
        self.fill_registration_form(link2)


if __name__ == "__main__":
    unittest.main()