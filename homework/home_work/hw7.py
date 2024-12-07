from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    new = browser.window_handles[1]
    browser
    first_name = browser.find_element(By.NAME,'firstname')
    first_name.send_keys("Lenovo")
    last_name = browser.find_element(By.NAME,'lastname')
    last_name.send_keys('Idealpad')
    email = browser.find_element(By.NAME,'email')
    email.send_keys('example@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(r"C:\Users\Elshad\PycharmProjects\Training\example.txt"))
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    print("good")
finally:
    time.sleep(5)
    browser.quit()




