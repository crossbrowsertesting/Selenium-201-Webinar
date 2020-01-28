# need the webdriver object
from selenium import webdriver

# example of using By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginForm import LoginForm

import time

def create_driver():
    return webdriver.Chrome('chromedriver')

def test_live():
    driver = create_driver()

    driver.get('https://app.crossbrowsertesting.com/login')
    login_form = LoginForm(driver)
    login_form.login()


    # this might make more sense in a LiveTest class
    wait = WebDriverWait(driver, 5)
    url_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-se-id="liveTestUrl"]')))

    driver.find_element(By.NAME, 'address').send_keys("https://crossbrowsertesting.com")

    time.sleep(5)
    driver.quit()


def test_selenium():
    driver = create_driver()

    driver.get('https://app.crossbrowsertesting.com/login')
    login_form = LoginForm(driver)
    login_form.login()

    driver.get('https://app.crossbrowsertesting.com/selenium/run')

    wait = WebDriverWait(driver, 5)
    desktop_os = wait.until(EC.presence_of_element_located((By.ID, 'desktop-os')))

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    print("Testing the Live test page")
    test_live()
    print("Testing the Automation test page")
    test_selenium()
    print("All tests passed!")




