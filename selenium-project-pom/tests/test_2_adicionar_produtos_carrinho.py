import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# adicionando mochila ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()

# verificando que a mochila foi adicionada
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# clicando em voltar para a tela de produtos
driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

# adicionando mais um produto ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()

# verificando se os dois produtos estão no carrinho
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

