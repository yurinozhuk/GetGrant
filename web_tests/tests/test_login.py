from web_tests.pages.login_page import LoginPage
from web_tests.tests.base_test import BaseTest
from web_tests.pages.common_xpath_locators import LoginPageLocators
from web_tests.utilities.assert_utils import AssertionUtils
from web_tests.utilities.driver_utils import close_driver
from web_tests.utilities.logger import log


class TestLogin(BaseTest,LoginPageLocators):
    def test_click_login_button(self):
        login_page = LoginPage(self.driver)
        login_page.mouse_over_login_button()
        login_page.click_login_button()
        log.info("Clicked the login button")
        assert AssertionUtils.not_empty(login_page), "Login page object should not be empty."
        close_driver(self.driver)



    #
    # # just example how open other pages
    # def test_open_new_window(self):
    #     self.driver.get("https://google.com")
