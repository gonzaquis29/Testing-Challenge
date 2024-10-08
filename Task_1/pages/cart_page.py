from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.driver.get("https://demo.evershop.io/")

    
    def go_to_checkout(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']")))
        checkout_button.click()

    