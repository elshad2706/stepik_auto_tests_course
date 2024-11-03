import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By


class test_class_name(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test method
        self.browser = webdriver.Chrome()  # You can use any other webdriver here

    def tearDown(self):
        # This method will be called after each test method
        self.browser.quit()
    def test_registration_page1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код для заполнения формы на странице
        button1 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        button1.send_keys("Name")
        button2 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        button2.send_keys("Surname")
        button3 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        button3.send_keys("test@mail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # Проверка, что после заполнения формы нет ошибок
        self.assertEqual(welcome_text,'Congratulations! You have successfully registered!','correct')

    def test_registration_page2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код для заполнения формы на странице

        button1 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        button1.send_keys("Name")
        button2 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        button2.send_keys("Surname")
        button3 = self.browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        button3.send_keys("test@mail.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # Проверка, что после заполнения формы есть ошибка (NoSuchElementException)
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'correct')


if __name__ == "__main__":
    browser = webdriver.Chrome()
    unittest.main()
