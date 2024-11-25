import pytest
from selenium import webdriver
from registration_page import RegistrationPage
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    yield driver
    driver.quit()


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.filling_forms(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    submit_button = RegistrationPage(driver)
    submit_button.submit_form()

    zip_code_fields = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert "alert-danger" in zip_code_fields.get_attribute("class")

    green_backlight = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    assert len(green_backlight) == 9
