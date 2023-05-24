
from selenium.webdriver.common.by import By

INPUT_EMAIL = 'username'
INPUT_PASSWORD = 'password'
BUTTON_LOGIN = '.c79fd81e4 > button'
CHECKBOX_CAPTCHA = '[class="recaptcha-checkbox-checkmark"]'

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, url, username, password):
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element(By.ID, INPUT_EMAIL).send_keys(username)
        self.driver.find_element(By.ID, INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, BUTTON_LOGIN).click()
