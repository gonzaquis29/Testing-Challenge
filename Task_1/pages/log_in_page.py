from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogInPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click_create_account_link(self):
        account_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/account/register']")))
        account_link.click()

    def create_account(self, full_name, email, password):
        full_name_input = self.wait.until(EC.presence_of_element_located((By.NAME, "full_name")))
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        
        submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.primary[type='submit']")))

        full_name_input.send_keys(full_name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
     