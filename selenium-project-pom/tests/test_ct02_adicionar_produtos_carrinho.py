import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"

        # fazer login
        login_page.fazer_login("standard_user","secret_sauce")

        # adicionando mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # clicando em voltar para a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        # adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # verificando se os dois produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

