from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()