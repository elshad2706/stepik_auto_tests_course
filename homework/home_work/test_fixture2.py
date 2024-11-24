import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture
def browser():
    link = "https://belurk.pro/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    yield browser
    browser.quit()

class Test_Basic_auth():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_signin(self, browser):
        vxod = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/signin"]'))
        )
        vxod.click()
        login = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        login.send_keys("elshadqa2720@gmail.com")
        password = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password.send_keys("Easy777!")
        submit = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
        )
        time.sleep(1)
        submit.click()
        welcome_text_elt = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".lg\:text-\[52px\]"))
        )
        welcome_text = welcome_text_elt.text
        assert "Мои прокси" == welcome_text
        print('Тест пройден')

# link = "http://selenium1py.pythonanywhere.com/"
# @pytest.fixture(scope=)#задать уровень фикстуры (scope). Возможные значения “function”, “cls”, “module”, “session”. Значение по умолчанию = “function”.
# def browser():
#     browser = webdriver.Chrome()
#     print("xtnj xt nsng")
#     yield browser
#     print("закрываем")
#     browser.quit()
#
#
# class Basic_auth():
#     @pytest.mark.smoke
#     def signin(self,browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#         print("тест идет")

