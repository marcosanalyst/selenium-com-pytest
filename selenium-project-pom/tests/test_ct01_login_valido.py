import pytest
from selenium.webdriver.common.by import By
# importo o contest para uso e instancio as variaveis
import conftest
from pages.login_page import LoginPage

#aqui indico que ele está usando o setup_teardown
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
# toda classe devo iniciar com Test
class TestCT01:
    def test_ct01_login_valido(self):
        driver = conftest.driver
        # criando uma cópia de login_page para dentro deste teste
        login_page = LoginPage()
        # login DEPOIS
        login_page.fazer_login("standard_user","secret_sauce")

        # fazendo login ANTES
        # driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        # driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        # driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()