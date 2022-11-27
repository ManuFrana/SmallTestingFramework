import os.path

import pytest as pytest
from selenium import webdriver
import warnings
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request, browser):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise AssertionError("Invalid browser name:" + browser)
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driverWait = WebDriverWait(driver, 3)
    driver.get("https://duckduckgo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = driverWait
    yield request.cls.driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="specify the browser you want to use (chrome, firefox, edge)")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "SoutherCode Tests Reports"


