from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    sunduk = browser.find_element(By.ID,"treasure")
    sunduk_atribute = sunduk.get_attribute("valuex")
    print("значение атрибута", sunduk_atribute)
    assert sunduk_atribute is not None

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(sunduk_atribute)

    input_text = browser.find_element(By.ID,"answer")
    input_text.send_keys(y)
    time.sleep(1)
    robot_checkbox = browser.find_element(By.ID,"robotCheckbox")
    robot_checkbox.click()
    time.sleep(1)
    robots_Rule = browser.find_element(By.ID,"robotsRule")
    robots_Rule.click()
    time.sleep(1)
    submit = browser.find_element(By.CSS_SELECTOR,"button")
    submit.click()
    time.sleep(3)

finally:
    browser.quit()
