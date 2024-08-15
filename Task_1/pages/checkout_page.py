from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import random
import time
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://demo.evershop.io/cart")
    def click_checkout_page(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']")))
        checkout_button.click()

    def fill_shipping_address(self, customer_data):
        self.wait.until(EC.presence_of_element_located((By.NAME, "address[full_name]"))).send_keys(customer_data['full_name'])
        self.wait.until(EC.presence_of_element_located((By.NAME, "address[telephone]"))).send_keys(customer_data['telephone'])
        self.wait.until(EC.presence_of_element_located((By.NAME, "address[address_1]"))).send_keys(customer_data['address_1'])
        self.wait.until(EC.presence_of_element_located((By.NAME, "address[city]"))).send_keys(customer_data['city'])
       
        country_element = self.wait.until(EC.presence_of_element_located((By.ID, "address[country]")))
        select = Select(country_element)

        # I tested several countries and selected China because it works but it asks for additional information
        select.select_by_index(2)
        time.sleep(2)
        
        province_element = self.wait.until(EC.presence_of_element_located((By.ID, "address[province]")))
        select_p = Select(province_element)
        select_p.select_by_index(1)

        self.wait.until(EC.presence_of_element_located((By.NAME, "address[postcode]"))).send_keys(customer_data['postcode'])
        
        time.sleep(2) 
        # Select radio button for shipping method
        radio_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='method1']")))
        # Click the button
        radio_button.click()

        
        # Click the "Continue to payment" button
        time.sleep(2)
        continue_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.primary span'))) 
        continue_button.click()
            
        

    def fill_payment_information(self):

        time.sleep(4)
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkoutPaymentForm"]/div[3]/div[1]/div/div/div/div[1]/a'))) 
        continue_button.click()
        
        time.sleep(4)

        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.primary span'))) 
        place_order_button.click()
        


    def verify_order_details(self, customer_data):
        # Expected values from the test data
        expected_full_name = customer_data['full_name']
        expected_email = customer_data['email']
        expected_shipping_address = customer_data['address_1']

        # Locators for elements on the order confirmation page
        full_name_locator = (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]')
        email_locator = (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[1]/div[3]')
        full_name_address_locator = (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[1]')
        full_name_billing_address_locator = (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div[1]')

        payment_method_locator = (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]')

        item_name_locator = (By.CSS_SELECTOR, "table.listing.items-table td")

        # Get the actual values from the order confirmation page
        actual_full_name = self.wait.until(EC.presence_of_element_located(full_name_locator)).text
        actual_email = self.wait.until(EC.presence_of_element_located(email_locator)).text
        actual_payment_method = self.wait.until(EC.presence_of_element_located(payment_method_locator)).text
        actual_full_name_address_locator = self.wait.until(EC.presence_of_element_located(full_name_address_locator)).text
        actual_full_name_billing_address_locator = self.wait.until(EC.presence_of_element_located(full_name_billing_address_locator)).text

        items_elements = self.wait.until(EC.presence_of_all_elements_located(item_name_locator))

        # Assertions
        assert actual_full_name == expected_full_name, f"Expected full name {expected_full_name}, but got {actual_full_name}"
        print("Full name is correct.")

        assert actual_email == expected_email, f"Expected email {expected_email}, but got {actual_email}"
        print("Expected email is correct.")

        assert actual_full_name_address_locator != "", f"Shipping Address exists"
        print("There is information for Shipping Address")

        assert actual_full_name_billing_address_locator != "", f"Billing Address exists"
        print("There is information for Billing Address")
        
        assert actual_payment_method != "", f"Payment Method does not exist"
        print("Payment method exists")

        # Items validation
        # I count number of tds as it suggest the existence of items
        td_count = len(items_elements)

        assert td_count > 0, f"There are no items in this order"
        print("There are items in this order")