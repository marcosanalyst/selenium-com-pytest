import time

import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # fazer login
        login_page.fazer_login("standard_user","secret_sauce")

        # adicionando mochila ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        # # clicando em voltar para a tela de produtos
        # driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()
        #
        # # adicionando mais um produto ao carrinho
        # driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        # driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        #
        # # verificando se os dois produtos estão no carrinho
        # driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        #
