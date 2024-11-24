import  pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *
from fixtures import *
import time
import math

@pytest.mark.parametrize('link',[link_1,link_2,link_3,link_4,link_5,link_6,link_7,link_8])
class TestLogin:
    def test_authorization(self,browser,link,load_config):
        login_stepik = load_config['login_stepik']
        password_stepik = load_config['password_stepik']
        browser.get(link)
        browser.maximize_window()
        signin = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID,sign_in))
        ).click()
        email = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID,input_email)))
        email.send_keys(login_stepik)
        password = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.ID,input_password)))
        password.send_keys(password_stepik)
        password.send_keys(Keys.RETURN)
        browser.implicitly_wait(10)
        input_answer = WebDriverWait(browser,15).until(
            EC.presence_of_element_located((By.XPATH, text_area))
        )
        clear_area = input_answer.clear()
        answer = str(math.log(int(time.time())))
        time.sleep(4)
        #вот здесь как то надо ждать,пока полностью загрузится страница,надо разбираться в чем проблема
        input_answer.send_keys(answer)
        send_button = WebDriverWait(browser,15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,send))
        ).click()
        correct_message = WebDriverWait(browser,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,correct_answer))).text()
        compare('Correct!',correct_message)


