import time

from conftest import *

def test_auth(browser):
    sign_in = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ember420'))
    )
    sign_in.click()
    login = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.ID,'id_login_email'))
    )
    login.send_keys('elshadmursalov8@gmail.com')
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'id_login_password'))
    )
    password.send_keys('Snik1995s')
    vxod = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div/div[1]/div/form/button'))
    )
    vxod.click()
    time.sleep(50000)
    input_answer = WebDriverWait(browser,10).until(
        EC.presence_of_element_located(By.ID,'ember479')
    )
    input_answer.send_keys(answer)
    submit = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'submit-submission'))
    )
    submit.click()
