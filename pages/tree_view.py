import time

from selenium.webdriver.common.by import By


class TreeView:
    def __init__(self, driver):
        self.driver = driver

    def open_specific_number_rapport_and_question(self, number):
        self.driver.find_element(By.CSS_SELECTOR, 'aside > div div:nth-child('+number+') > div > div').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'aside > div div:nth-child('+number+') > div li div > p.MuiTypography-root.MuiTypography-body1.css-1w67cpv').click()

