from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demo.evershop.io/")

    def click_log_in_icon(self):
        account_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/account/login']")))
        account_icon.click()