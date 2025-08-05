import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='{}']")

    def verificar_produto_carrinho_existe(self, nome_item):
        # By. está na posição zero e Locator está na posição 1
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)
