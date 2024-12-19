import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import allure


@pytest.fixture()
def driver():
    with allure.step("Запуск драйвера"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        yield driver
    with allure.step("Закрытие драйвера"):
        driver.quit()


@allure.severity("blocker")
@allure.title("Работа калькулятора")
@allure.feature("Калькулятор")
@allure.description("Тест выполняет математические операции, с установленной задержкой времени")
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятор"):
        calculator_page = CalculatorPage(driver)
        calculator_page.enter_delay_value('4')
        calculator_page.click_button("7")
        calculator_page.click_operator_button("+")
        calculator_page.click_button("8")
        calculator_page.click_equals_button()

    result = calculator_page.get_result()
    with allure.step('Проверить, что результат совпадает'):
        assert result == "15"
