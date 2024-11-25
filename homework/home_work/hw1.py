from selenium import webdriver
from selenium.webdriver.common.by import By
from fixtures import compare
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR,"#answer")
    answer_input.send_keys(y)
    time.sleep(2)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
    robot_checkbox.click()
    time.sleep(2)
    texter = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/form/div[4]/label'))).text
    print(texter)
    compare('Robots rule', texter)
    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    robots_rule_radiobutton.click()
    time.sleep(2)
    submit_button = browser.find_element(By.CSS_SELECTOR,"button")
    submit_button.click()
    time.sleep(3)
finally:
    time.sleep(5)
    browser.quit()

