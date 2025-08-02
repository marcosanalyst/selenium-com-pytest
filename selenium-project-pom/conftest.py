import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test 'return', vai rodar até este ponto quando chamado, depois executa o que está abaixo (tear_down)
    yield

    # teardown
    driver.quit()