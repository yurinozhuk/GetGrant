import os

import allure

from web_tests.pages.base_page import BasePage
from web_tests.pages.common_xpath_locators import LoginPageLocators
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click login button")
    def click_login_button(self):
        self.click_element(("xpath", LoginPageLocators.LOGIN_BUTTON))

    def mouse_over_login_button(self):
        self.mouse_over(LoginPageLocators.LOGIN_REGISTER_BTNS)

    def input_email(self, email):
        self.click_element(("xpath", LoginPageLocators.EMAIL_INPUT))
        web_element = self.get_element(("xpath", LoginPageLocators.EMAIL_INPUT))
        web_element.send_keys(email)

    def input_password(self, password):
        self.click_element(("xpath", LoginPageLocators.PASSWORD_INPUT))
        web_element = self.get_element(("xpath", LoginPageLocators.PASSWORD_INPUT))
        web_element.send_keys(password)

    def click_sign_in_button(self):
        self.click_element(("xpath", LoginPageLocators.SIGN_IN_BUTTON))
