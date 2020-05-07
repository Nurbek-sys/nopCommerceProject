import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Launching the Chrome browser")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("Laucnhing the Firefox browser")
    return driver

def pytest_addoption(parser):     #### This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):             #### This will return the Browser value to setup method
    return request.config.getoption("--browser")


# Pytest Report generation
# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nurbek'


# It is hook for delete / Modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)