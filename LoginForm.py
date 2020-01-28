from selenium.webdriver.common.by import By
import unittest
from creds import creds

class LoginForm:
    def __init__(self, driver):
        self.driver = driver
        self.title = "CrossBrowserTesting App"
        self.email_address = creds.email_address.value
        self.password = creds.password.value

        self.email_address_locator = 'inputEmail'
        self.password_locator = 'password'
        self.submit_button_locator = 'button[data-se-id="login-btn"]'
    
    def title_matches(self):
        return self.title == self.driver.title

    def login(self):
        assert self.title_matches()

        username_field = self.driver.find_element(By.ID, self.email_address_locator)
        username_field.send_keys(self.email_address)

        password_field = self.driver.find_element(By.NAME, self.password_locator)
        password_field.send_keys(self.password)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, self.submit_button_locator)
        submit_button.click()

        