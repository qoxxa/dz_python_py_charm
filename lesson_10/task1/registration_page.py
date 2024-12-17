from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение формы данными {first_name} {last_name} {address} {email} {phone} {zip_code} {city} {country} {job_position} {company}')
    def filling_forms(self, first_name: str, last_name: str, address: str, email: str, phone: int, zip_code: int, city: str, country: str, job_position: str, company: str):
        self.driver.find_element(By.CSS_SELECTOR, "[name=first-name]").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name=last-name]").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name=address]").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "[name=e-mail]").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[name=phone]").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "[name=zip-code]").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "[name=city]").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "[name=country]").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "[name=job-position]").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys(company)

    @allure.step('Клик по кнопке Submit')
    def submit_form(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]'))).click()
