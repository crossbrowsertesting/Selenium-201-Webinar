from selenium.webdriver.common.by import By
import unittest

class LoginForm:
    def __init__(self, driver):
        self.driver = driver
        self.title = "Login Form - CrossBrowserTesting.com"
    
    def title_matches():
        return self.title = self.driver.title

    def login(self):
        assert self.title_matches()

        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_text("tester@crossbrowsertesting.com")

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_text("test123")

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#submit")
        submit_button.click()

        