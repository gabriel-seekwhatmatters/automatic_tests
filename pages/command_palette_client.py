from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class CommandPaletteClient:
    def __init__(self, driver):
        self.driver = driver

    def clean_text_from_client(self):
        self.driver.find_element(By.CSS_SELECTOR,'#root > div.MuiBox-root.css-1pco6v8 > div > div > main > div > div > div.MuiBox-root.css-bgpqg > div > div.MuiBox-root.css-bpra72 > div > div > div > section > div > div > div.overflow-guard > textarea').send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(By.CSS_SELECTOR,'#root > div.MuiBox-root.css-1pco6v8 > div > div > main > div > div > div.MuiBox-root.css-bgpqg > div > div.MuiBox-root.css-bpra72 > div > div > div > section > div > div > div.overflow-guard > textarea').send_keys(Keys.DELETE)

    def write_text_client(self, sql):
        self.driver.find_element(By.CSS_SELECTOR,'#root > div.MuiBox-root.css-1pco6v8 > div > div > main > div > div > div.MuiBox-root.css-bgpqg > div > div.MuiBox-root.css-bpra72 > div > div > div > section > div > div > div.overflow-guard > textarea').send_keys(sql)
