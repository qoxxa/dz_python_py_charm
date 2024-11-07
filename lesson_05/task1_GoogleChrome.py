from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

delete_button = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_button))
sleep(5)
