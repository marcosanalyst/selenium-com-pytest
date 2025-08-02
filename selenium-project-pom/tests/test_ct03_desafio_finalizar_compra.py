import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.compra

class TestCT03:
    def test_ct03_desafio_finalizar_compra(self):
        driver = conftest.driver
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("locked_out_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # adicionando mochila ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()

        # verificando que a mochila foi adicionada
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # clicando em voltar para a tela de produtos
        driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

        # adicionando mais um produto ao carrinho
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[@id='add-to-cart']").click()

        # verificando se os dois produtos estão no carrinho
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # fazendo checkout
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        # preenchendo os dados
        driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Marcos")
        driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Silva")
        driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("00000-001")

        # clicar no botão Continue
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        # clicar no botão Finish
        driver.find_element(By.XPATH, "//button[@id='finish']").click()

        # validando mensagem de compra
        assert driver.find_element(By.XPATH, "//h2[.='Thank you for your order!']").is_displayed()








