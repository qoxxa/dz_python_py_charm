import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

#Test
def test_form_and_submit(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name=first-name]')
    first_name.clear()
    first_name.send_keys('Иван')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name=last-name]')
    last_name.clear()
    last_name.send_keys('Петров')

    address = driver.find_element(By.CSS_SELECTOR, 'input[name=address]')
    address.clear()
    address.send_keys('Ленина, 55-3')

    email = driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]')
    email.clear()
    email.send_keys('test@skypro.com')

    phone = driver.find_element(By.CSS_SELECTOR, 'input[name=phone]')
    phone.clear()
    phone.send_keys('+7985899998787')

    city = driver.find_element(By.CSS_SELECTOR, 'input[name=city]')
    city.clear()
    city.send_keys('Москва')

    country = driver.find_element(By.CSS_SELECTOR, 'input[name=country]')
    country.clear()
    country.send_keys('Россия')

    job = driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]')
    job.clear()
    job.send_keys('QA')

    company = driver.find_element(By.CSS_SELECTOR, 'input[name=company]')
    company.clear()
    company.send_keys('SkyPro')

#Нажатие кнопки Submit
    WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]'))
    ).click()

#Проверка подсветки
    zip_code_fields = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert "alert-danger" in zip_code_fields.get_attribute("class")

    green_backlight = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    assert len(green_backlight) == 9
