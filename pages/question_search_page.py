from selenium.webdriver.common.by import By


class QuestionSearchPage:

    def __init__(self, driver):
        self.driver = driver

    def select_specific_client_from_dropdown(self, client):
        self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div > div > button > svg > path').click()
        elements = self.driver.find_elements_by_css_selector('[role="listbox"] li')

        for element in elements:
            if client in element.text:
                element.click()

