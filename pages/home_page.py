import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def create_new_report(self, name, details):
        open_create_item_modal = self.driver.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-1ykox53 > button:nth-child(2) > svg').click()
        select_stack_option = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Create Item tabs"] [id="simple-tab-1"]').click()
        type_report_name = self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Stack Title"]').send_keys(name)
        type_details = self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Type stack details here"]').send_keys(details)
        create_report_button = self.driver.find_element(By.CSS_SELECTOR, '#simple-tabpanel-1 button').click()


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
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.MuiBox-root.css-1ykox53 > button:nth-child(2) > svg')))
        open_create_item_modal = self.driver.find_element(By.CSS_SELECTOR,'div.MuiBox-root.css-1ykox53 > button:nth-child(2) > svg').click()
        type_question_name = self.driver.find_element(By.CSS_SELECTOR, '[placeholder="Type your question here"]').send_keys(name)
        select_report = self.driver.find_element(By.CSS_SELECTOR, 'ul > div:nth-child(6) input').click()
        create_button = self.driver.find_element(By.CSS_SELECTOR, '#simple-tabpanel-0 > div > button').click()

    def regenerate_question(self):
        press_regenerate_question = self.driver.find_element(By.CSS_SELECTOR, 'section > div.MuiBox-root.css-1cdb226 > button').click()

    def clean_text(self):
        # box = self.driver.find_element(By.CSS_SELECTOR,
        #                     'div.margin-view-overlays > div:nth-child(1) > div.cldr.alwaysShowFoldIcons.codicon.codicon-folding-expanded')
        # box.click()

        row = self.driver.find_element(By.CSS_SELECTOR,'div:nth-child(2) > span > span').click()
        row = self.driver.find_element(By.CSS_SELECTOR,'div:nth-child(3) > span > span').click()
        row = self.driver.find_element(By.CSS_SELECTOR,'div:nth-child(4) > span > span').click()

        time.sleep(5)
        # row.send_keys(Keys.CONTROL, 'a')
        # time.sleep(10)
        t = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > span > span').send_keys(Keys.BACK_SPACE)
        t = self.driver.find_element(By.CSS_SELECTOR, '.overflow-guard').send_keys(Keys.F1)

        time.sleep(10)


