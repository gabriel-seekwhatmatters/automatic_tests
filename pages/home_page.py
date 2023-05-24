import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def create_new_report(self, name, details):
        self.driver.find_element(By.CSS_SELECTOR, '.css-1ykox53 > button > svg').click()
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Create Item tabs"] [id="simple-tab-1"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Stack Title"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Type stack details here"]').send_keys(details)
        self.driver.find_element(By.CSS_SELECTOR, '#simple-tabpanel-1 button').click()


    def get_report_position(self):
        # Find the list element
        list_element = self.driver.find_element(By.CSS_SELECTOR,'#simple-tabpanel-1 ul > div > div > div')

        # Get the text of the element you want to find the position of
        element_text = 'Testing report'

        # Find all the elements in the list using a CSS selector
        list_items = list_element.find_elements_by_css_selector('*')

        # Find the position of the element with the specified text
        position = 0
        for i, item in enumerate(list_items):
            if item.text == element_text:
                position = i
                break

        # Print the position
        print(f"The position of '{element_text}' is: {position}")

    def create_new_question(self,name):
        self.driver.refresh()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,'.css-1ykox53 > button > svg').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.MuiPaper-root [type="text"]').send_keys(name)
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, 'ul > div:nth-child(5) input').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '#simple-tabpanel-0 > div > button').click()
        time.sleep(15)

    def regenerate_question(self):
        self.driver.find_element(By.CSS_SELECTOR, 'section > div.MuiBox-root.css-1cdb226 > button').click()

    def clean_text(self):
        row = self.driver.find_element(By.CSS_SELECTOR,'.view-lines')
        row.click()

        time.sleep(5)
        row.send_keys(Keys.DELETE)
        time.sleep(10)


