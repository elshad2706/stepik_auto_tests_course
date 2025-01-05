import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
import json


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config


def compare(expected, actual):
    try:
        assert expected == actual
    except AssertionError:
        print(f"expected {expected}, not equal  {actual}")

