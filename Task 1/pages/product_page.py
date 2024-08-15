from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains
import time
class ProductPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_random_category(self):
        categories = ["kids", "men", "women"]
        category = random.choice(categories)
        category_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[href='/{category}']")))
        category_button.click()

    def select_random_product(self):
        product_links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-name a")))
        random_product = random.choice(product_links)
        random_product.click()
    
    def set_random_size_and_color(self):
        option_lists = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".variant-option-list")))
        size_list = option_lists[0]
        color_list = option_lists[1]

        # Get all size options
        size_options = size_list.find_elements(By.TAG_NAME, "li")
        # Select a random size
        random_size = random.choice(size_options)
        random_size.find_element(By.TAG_NAME, "a").click()

        time.sleep(2)
        # Get all color options
        color_options = color_list.find_elements(By.TAG_NAME, "li")
        # Select a random color
        random_color = random.choice(color_options)
        random_color.find_element(By.TAG_NAME, "a").click()

    def set_random_size(self):
        # Espera a que los elementos <li> de las tallas estén presentes
        size_options = self.wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[2]/div/div[2]/div[2]/div[1]/ul/li')))
    
        # Verifica si las opciones están disponibles
        if size_options:
            # Selecciona aleatoriamente un <li> de la lista de tamaños
            random_size_li = random.choice(size_options)
            size_option_link = random_size_li.find_element(By.TAG_NAME, "a")
            # Haz clic en el enlace dentro del <li> seleccionado
            size_option_link.click()
            print(f"Selected size: {size_option_link.text}")
        else:
            print("No size options available.")


    def set_random_color(self):
        # Wait until colors are present
        color_options = self.wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//*[@id="app"]/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li')))
    
        # Verify if options are available
        if color_options:
            random_color_li = random.choice(color_options)
            color_option_link = random_color_li.find_element(By.TAG_NAME, "a")
            color_option_link.click()
            print(f"Selected color: {color_option_link.text}")
        else:
            print("No color options available.")

    def set_random_quantity(self):
        # Select random quantity for product from 1 to 10
        quantity_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='qty']")))
        quantity = random.randint(1, 10)
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.primary.outline")))
        add_to_cart_button.click()

    
    def add_random_products_to_cart(self, num_products):
        for _ in range(num_products):
            # Start from the home page
            self.driver.get("https://demo.evershop.io/")

            # Select a random category (kid, men, or women)
            self.select_random_category()

            # Select a random product from the category page
            self.select_random_product()
         

            # On the product page, select size, color, and quantity
            self.set_random_quantity()
            time.sleep(1)

            self.set_random_size_and_color()
            
            time.sleep(1)

            # Add the product to the cart
            self.add_to_cart()

            