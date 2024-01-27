import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By


def test_registration_page1():
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код для заполнения формы на странице
        button1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        button1.send_keys("Name")
        button2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        button2.send_keys("Surname")
        button3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        button3.send_keys("test@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # Проверка, что после заполнения формы нет ошибок
        assert(welcome_text,'Congratulations! You have successfully registered!','correct')
        browser.quit()

def test_registration_page2():
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        # Ваш код для заполнения формы на странице
        button1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        button1.send_keys("Name")
        button2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        button2.send_keys("Surname")
        button3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        button3.send_keys("test@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # Проверка, что после заполнения формы есть ошибка (NoSuchElementException)
        assert(welcome_text, 'Congratulations! You have successfully registered!', 'correct')
        browser.quit()

if __name__ == "__main__":
    pytest.main()
