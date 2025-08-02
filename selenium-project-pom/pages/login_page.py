import conftest
from selenium.webdriver.common.by import By

class LoginPage:
    # construtor da classe
    def __init__(self):
        self.driver = conftest.driver

    def fazer_login(self, usuario, senha):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(usuario)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(senha)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()