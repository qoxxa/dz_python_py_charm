from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceMainPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, name, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_products(self):
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def personal_data(self, name, last_name, index):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def total_cost(self):
        txt = WebDriverWait(self.driver, "10").until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        return txt

