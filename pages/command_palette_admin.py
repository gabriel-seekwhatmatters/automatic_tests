from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class CommandPaletteAdmin:
    def __init__(self, driver):
        self.driver = driver

    def clean_text_admin(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div:nth-child(2) > div.MuiBox-root.css-8sv8ev > div > div > section > section.studio__codeEditor > div > div > section > div > div > div.overflow-guard > textarea').send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR, '#root > div:nth-child(2) > div.MuiBox-root.css-8sv8ev > div > div > section > section.studio__codeEditor > div > div > section > div > div > div.overflow-guard > textarea').send_keys(Keys.DELETE)

    def write_text_admin(self, sql):
        self.driver.find_element(By.CSS_SELECTOR,'#root > div:nth-child(2) > div.MuiBox-root.css-8sv8ev > div > div > section > section.studio__codeEditor > div > div > section > div > div > div.overflow-guard > textarea').send_keys(sql)

    def check_current_command_palette(self, customer):
        span_element = self.driver.find_element(By.CSS_SELECTOR,'aside > section > div.questions-container > div > div.accordion__item.curser-pointer.accordion__item--active > div:nth-child(2) > span')

        # Get the text inside the <span> element
        span_text = span_element.text

        # Print the text
        assert span_text == customer

