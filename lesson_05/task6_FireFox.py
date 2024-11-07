from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/login')

username = driver.find_element(By.NAME, 'username')
username.send_keys('tomsmith')

password = driver.find_element(By.NAME, 'password')
password.send_keys('SuperSecretPassword!')

login = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login.click()
sleep(3)
driver.quit()
