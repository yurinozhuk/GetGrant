import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from web_tests.configs.config import Config
from web_tests.pages.login_page import LoginPage
from web_tests.utilities.driver_utils import get_driver, close_driver


@pytest.fixture()
def driver(request):
    """
    Fixture to initialize and return the WebDriver instance.
    """
    driver = get_driver()
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    yield driver
    close_driver(driver)


@pytest.fixture()
def login_page(driver):
    """
    Fixture to initialize and return the LoginPage instance.
    """
    return LoginPage(driver)


# Screenshot makers
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Pytest hook implementation to capture and attach screenshots to Allure report for failed test cases using WebDriver.
    """
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        for value in item.funcargs.values():
            if isinstance(value, WebDriver):
                data = value.get_screenshot_as_png()
                allure.attach(body=data, name=item.name, attachment_type=allure.attachment_type.PNG)
                break
