from selenium.webdriver.common.by import By


class TopBar:

    def __init__(self, driver):
        self.driver = driver

    def open_studio(self):
        studio_button = self.driver.find_element(By.CSS_SELECTOR, '#root > header a:nth-child(4) > button > svg').click()