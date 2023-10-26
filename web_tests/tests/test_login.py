import os

import allure

from web_tests.configs.config import Config
from web_tests.pages.login_page import LoginPage
from web_tests.tests.base_test import BaseTest
from web_tests.pages.common_xpath_locators import LoginPageLocators
from web_tests.utilities.assert_utils import AssertionUtils
from web_tests.utilities.driver_utils import close_driver
from web_tests.utilities.logger import log
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')


class TestLogin(BaseTest, LoginPageLocators):
    def test_click_login_button(self):
        login_page = LoginPage(self.driver)
        login_page.select_language()
        login_page.mouse_over_login_button()
        login_page.click_login_button()
        login_page.input_email(EMAIL)
        login_page.input_password(PASSWORD)
        login_page.click_sign_in_button()

        assert AssertionUtils.contains_any(LoginPageLocators.PRIVATE_CONTAINER,
                                           "Login page object should not be empty.")
        log.info("User is logged in")

        close_driver(self.driver)

    #
    # # just example how open other pages
    # def test_open_new_window(self):
    #     self.driver.get("https://google.com")
