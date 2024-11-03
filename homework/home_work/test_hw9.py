import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def prepare_faces():
    browser = webdriver.Chrome()
    print("^_^", "\n")
    yield
    print(":3", "\n")
    browser.quit()


@pytest.fixture()
def very_important_fixture():
    browser = webdriver.Chrome()
    print(":)", "\n")
    browser.quit()


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture,browser):
        browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("test1")

    def test_second_smiling_faces(self, prepare_faces,browser):
        browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("test2")