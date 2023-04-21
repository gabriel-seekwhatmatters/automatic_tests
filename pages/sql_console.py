import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

CONSOLE_SPACE = '#root > div:nth-child(2) > div.MuiBox-root.css-8sv8ev > div > div > section > section.studio__codeEditor > div > div > section > div > div > div.overflow-guard > textarea'
class SqlConsole:

    def __init__(self, driver):
        self.driver = driver

    def press_clear_console(self):
        console_content = self.driver.find_element(By.CSS_SELECTOR, CONSOLE_SPACE).send_keys(Keys.CONTROL + 'a')
        console_content = self.driver.find_element(By.CSS_SELECTOR, CONSOLE_SPACE).send_keys(Keys.DELETE)

    def type_in_console(self, content):
        console_content = self.driver.find_element(By.CSS_SELECTOR, CONSOLE_SPACE).send_keys(content)