import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INPUT_EMAIL = '[type=email]'
INPUT_PASSWORD = '[name="password"]'
BUTTON_LOGIN = '.login button'
CHECKBOX_CAPTCHA = '[class="recaptcha-checkbox-checkmark"]'

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, url, username, password):
        self.driver.maximize_window()
        self.driver.get(url)
        email_input = self.driver.find_element(By.CSS_SELECTOR, INPUT_EMAIL).send_keys(username)
        password_input = self.driver.find_element(By.CSS_SELECTOR, INPUT_PASSWORD).send_keys(password)
        #time.sleep(20)
        login_button = self.driver.find_element(By.CSS_SELECTOR, BUTTON_LOGIN).click()

    def login_admin(self, username):
        email_input = self.driver.find_element(By.CSS_SELECTOR, INPUT_EMAIL).send_keys(username)

        #password_input = self.driver.find_element(By.CSS_SELECTOR, INPUT_PASSWORD).send_keys(password)

        time.sleep(3)
        #login_button = self.driver.find_element(By.CSS_SELECTOR, BUTTON_LOGIN).click()
