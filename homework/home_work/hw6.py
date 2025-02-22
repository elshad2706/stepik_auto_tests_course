from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    Link = ('http://suninjuly.github.io/explicit_wait2.html')
    browser.get(Link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book = browser.find_element(By.CSS_SELECTOR, '#book').click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID,'answer')
    input.send_keys(y)
    submit = browser.find_element(By.ID,'solve').click()
finally:
    time.sleep(4)
    browser.quit()
