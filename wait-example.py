# need the webdriver object
from selenium import webdriver

# example of using By
from selenium.webdriver.common.by import By

# example of using Wait
from selenium.webdriver.support.ui import WebDriverWait

# example of using ExpectedConditions
from selenium.webdriver.support import expected_conditions as EC

def pause():
    input("Press any button to continue..")

# some boilerplate - create a webdriver using a local chromedriver binary
driver = webdriver.Chrome('./chromedriver')

# navigate to the crossbrowsertesting website
driver.get('https://app.crossbrowsertesting.com/login')

# find email field using its ID attribute
email_input = driver.find_element(By.ID, 'inputEmail')
email_input.send_keys("tester@crossbrowsertesting.com")

# find the password field using its name attribute
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys("test123")

# could use ID here.. but let's try using CSS selectors instead
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-se-id="login-btn"]')

print("Found the submit button")
print(dir(submit_button))
pause()

submit_button.click()


"""

create a wait object that can be used 
to pause execution until an element is
present on the webpage. 

"""

wait = WebDriverWait(driver, 10)
url_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-se-id="liveTestUrl"]')))

print("URL Bar for Live Testing found!")
print(dir(url_bar))
pause()




driver.quit()