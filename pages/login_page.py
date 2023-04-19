import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, url, username, password):
        self.driver.maximize_window()
        self.driver.get(url)
        email_input = self.driver.find_element(By.CSS_SELECTOR, '[type=email]').send_keys(username)
        password_input = self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
        time.sleep(2)
        login_button = self.driver.find_element(By.CSS_SELECTOR, '#root > div.login > div > div.ui.segment.multi-page__stack1 > form > button').click()

    def login_admin(self, username):
        email_input = self.driver.find_element(By.CSS_SELECTOR, '[type=email]').send_keys(username)

        #password_input = self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)

        time.sleep(3)
        #login_button = self.driver.find_element(By.CSS_SELECTOR, '#root > div.login > div > div.ui.segment.multi-page__stack1 > form > button').click()
