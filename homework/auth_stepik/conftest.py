import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.get('https://stepik.org/lesson/236895/step/1')
    yield browser
    browser.quit()

