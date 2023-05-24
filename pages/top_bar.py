from selenium.webdriver.common.by import By

LOGOUT_BUTTON = '[crossorigin="anonymous"]'

class TopBar:

    def __init__(self, driver):
        self.driver = driver

    def open_studio(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > header a:nth-child(3) > button > svg').click()

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, LOGOUT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, 'li.MuiButtonBase-root.MuiMenuItem-root.MuiMenuItem-gutters.css-139k1de').click()
