import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT04:
    def test_ct04_desafio_validar_login_com_senha_invalida(self):
        driver = conftest.driver
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce99")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        # validar mensagem de credenciais inválidas
        assert driver.find_element(By.XPATH, "//*[@class='error-message-container error']").is_displayed()
