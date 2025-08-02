from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Credenciais
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce99")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# validar mensagem de credenciais inválidas
assert driver.find_element(By.XPATH, "//*[@class='error-message-container error']").is_displayed()
