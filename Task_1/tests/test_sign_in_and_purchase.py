import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.log_in_page import LogInPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import generate_customer_data

@pytest.mark.usefixtures("driver")
class TestSignInAndPurchase:
    def test_sign_in_and_purchase(self):
        # Generate test data
        customer_data = generate_customer_data()

        # Initialize page objects
        home_page = HomePage(self.driver)
        log_in_page = LogInPage(self.driver)
        product_page = ProductPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Test steps
        home_page.open()
        home_page.click_log_in_icon()

        log_in_page.click_create_account_link()

        log_in_page.create_account(customer_data['full_name'], customer_data['email'], customer_data['password'])

        # I am already logged in and I am in home page, then I will add products

        product_page.add_random_products_to_cart(3)

        checkout_page.open()
        checkout_page.click_checkout_page()

        checkout_page.fill_shipping_address(customer_data)
        checkout_page.fill_payment_information()

        # Assertions
 
        checkout_page.verify_order_details(customer_data)