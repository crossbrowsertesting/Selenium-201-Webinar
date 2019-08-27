# need the webdriver object
from selenium import webdriver

# example of using By
from selenium.webdriver.common.by import By

def pause():
    input("Press any button to continue..")

# some boilerplate - create a webdriver using a local chromedriver binary
driver = webdriver.Chrome('./chromedriver')

# navigate to the crossbrowsertesting website
driver.get('https://app.crossbrowsertesting.com/login')

print("We've arrived at the CrossBrowserTesting login form!")

# find email field using its ID attribute
email_input = driver.find_element(By.ID, 'inputEmail')

print("Found the email input element")
print(dir(email_input))
pause()

email_input.send_keys("tester@crossbrowsertesting.com")

# find the password field using its name attribute
password_input = driver.find_element(By.NAME, 'password')

print("Found the password input element")
print(dir(password_input))
pause()

password_input.send_keys("test123")

# could use ID here.. but let's try using CSS selectors instead
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-se-id="login-btn"]')

print("Found the submit button")
print(dir(submit_button))

submit_button.click()

driver.quit()