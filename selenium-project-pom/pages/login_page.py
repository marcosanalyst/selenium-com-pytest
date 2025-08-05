import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # construtor da classe
    def __init__(self):
        self.driver = conftest.driver
        super().__init__()
        self.username_field = (By.XPATH, "//input[@id='user-name']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")
        self.error_message_login = (By.XPATH, "//*[@class='error-message-container error']")

    def fazer_login(self, usuario, senha):
        # self.driver.find_element(*self.username_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.login_button).click()
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}' mas era esperado o texto '{texto_encontrado}'."


