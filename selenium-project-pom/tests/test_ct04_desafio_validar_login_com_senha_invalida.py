import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT04:
    def test_ct04_desafio_validar_login_com_senha_invalida(self):
        login_page = LoginPage()
        login_page.fazer_login("standard_user","senha_invalida")

        login_page.verificar_mensagem_erro_login()
