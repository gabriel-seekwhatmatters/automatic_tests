import time

from selenium.webdriver.common.by import By

LOGOUT_BUTTON = '[crossorigin="anonymous"]'

class TopBar:

    def __init__(self, driver):
        self.driver = driver

    def open_studio(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > header a:nth-child(3) > button > svg').click()

    def logout_client(self):
        self.driver.find_element(By.CSS_SELECTOR, LOGOUT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-139k1de').click()

    def logout_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="power off icon"]').click()
        time.sleep(5)

    def open_question_search_tab_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, '[href="/admin/question-search"]').click()