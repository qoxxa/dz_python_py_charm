from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

content = WebDriverWait(driver, 17).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
)

txt = (driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text)

print(txt)
driver.quit()
