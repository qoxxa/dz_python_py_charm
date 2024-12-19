import pytest
from selenium import webdriver
from saucedemo import SauceMainPage
import allure


@pytest.fixture()
def driver():
    with allure.step("Запуск драйвера"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/')
        yield driver
    with allure.step("Закрытие драйвера"):
        driver.quit()


@allure.title("Тест на работу с интернет-магазином")
@allure.description("Выбор товара, работа с корзиной и оплата")
@allure.feature("Интернет покупки")
@allure.severity("blocker")
def test_sauce(driver):
    sauce_page = SauceMainPage(driver)
    sauce_page.authorization('standard_user', 'secret_sauce')
    sauce_page.add_products()
    sauce_page.go_to_cart()
    sauce_page.personal_data('Pogodin', 'Konstantin', '195298')
    total_result = sauce_page.total_cost()

    price = 'Total: $58.29'
    with allure.step("Сравнить итоговую стоимость"):
        assert total_result == price
