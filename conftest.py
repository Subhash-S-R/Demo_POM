from selenium import webdriver
from time import sleep
import pytest

# browsers = ['chrome', 'firefox', 'edge']
# @pytest.fixture(params=browsers)
# def SAM(request):
#     browser = request.param
#     if browser.lower() == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser.lower() == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser.lower() == 'edge':
#         driver = webdriver.Edge()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get("https://demowebshop.tricentis.com/")
#     sleep(3)
#     yield driver
#     sleep(2)
#     driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', dest='browser', choices=['chrome', 'firefox', 'edge'])

@pytest.fixture
def SAM(request):
    print("Setup")
    browser = request.config.getoption("--browser")
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(3)
    yield driver
    print("TearDown")
    sleep(2)
    driver.close()
