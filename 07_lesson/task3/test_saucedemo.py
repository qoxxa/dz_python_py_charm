import pytest
from selenium import webdriver
from saucedemo import SauceMainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()


def test_sauce(driver):
    sauce_page = SauceMainPage(driver)
    sauce_page.authorization('standard_user', 'secret_sauce')
    sauce_page.add_products()
    sauce_page.go_to_cart()
    sauce_page.personal_data('Pogodin', 'Konstantin', '195298')
    total_result = sauce_page.total_cost()

    price = 'Total: $58.29'
    assert total_result == price
