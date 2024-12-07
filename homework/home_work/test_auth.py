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


@pytest.mark.('link',[link_1,link_2,link_3,link_4,link_5,link_6,link_7,link_8])
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
        browser.implicitly_wait(5)
        answer = str(math.log(int(time.time())))
        try:
            solve_again = WebDriverWait(browser,3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,solve_again_button))).click()
            alert = WebDriverWait(browser,5).until(
                EC.presence_of_element_located((By.XPATH,alert_confirm))).click()
            input_answer = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, text_area)))
            input_answer.send_keys(answer)
        except:
            input_answer = WebDriverWait(browser,3).until(
                EC.presence_of_element_located((By.XPATH, text_area)))
            input_answer.send_keys(answer)
        send_button = WebDriverWait(browser,5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,send))
        ).click()
        correct_message = WebDriverWait(browser,5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,correct_answer))).text
        list_message = []
        list_message.append(correct_message)
        print(list_message)
        compare('Correct!',correct_message)


