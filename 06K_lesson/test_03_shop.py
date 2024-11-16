import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Тест
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

#Открываем сайт
def test_shop(driver):
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

#Авторизация
    login = driver.find_element(By.CSS_SELECTOR, '#user-name')
    login.clear()
    login.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.clear()
    password.send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

#Добавление товаров
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

#Корзина и подтверждение
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

#Заполнение данных
    name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    name.clear()
    name.send_keys('Konstantin')

    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.clear()
    last_name.send_keys('Pogodin')

    zip = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    zip.clear()
    zip.send_keys('195298')
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

#Проверка суммы
    total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    price = "Total: $58.29"
    assert total == price
