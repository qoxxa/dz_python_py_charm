import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#Тест
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

#Заходим на сайт
def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

#Вводим в поле delay значение 45
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(45)

#Нажимаем кнопки
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

#Ожидаем результат 45 секунд
    waiter = WebDriverWait(driver, 46)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'),'15')
)

#Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    res = "15"
    assert result == res
