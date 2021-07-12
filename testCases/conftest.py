from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver")
        print("Launching Chrome browser...")
    else:
        driver = webdriver.Safari()
        print("Launching Safari browser...")
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata["Project Name"] = "Bunnings website"
    config._metadata["Module Name"] = "Search Functionality"
    config._metadata["Tester"] = "Naim Sihabuddin"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

