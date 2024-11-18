from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def browser_setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.get("https://www.imdb.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()