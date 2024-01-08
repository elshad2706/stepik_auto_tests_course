from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
    time.sleep(1)
    new_tab_handle = browser.window_handles[1]
    browser.switch_to.window(new_tab_handle)
    time.sleep(1)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID,'answer')
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR,'.btn.btn-primary').click()
finally:
    time.sleep(4)
    browser.quit()
