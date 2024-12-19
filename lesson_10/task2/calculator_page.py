from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    @allure.step('Запуск драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Установка задержки перед выполнением следующего шага {delay_value}")
    def enter_delay_value(self, delay_value: int):
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(delay_value)

    @allure.step("Ввод чисел в калькулятор {button_text}")
    def click_button(self, button_text: int):
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    @allure.step("Ввод математической операции {operator}")
    def click_operator_button(self, operator: str):
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    @allure.step("Клик по знаку =")
    def click_equals_button(self):
        equals_locator = f"//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    @allure.step("Получения результата")
    def get_result(self) -> str:
        WebDriverWait(self.driver, "46").until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
