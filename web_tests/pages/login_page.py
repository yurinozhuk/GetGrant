import allure
from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from web_tests.pages.common_xpath_locators import LoginPageLocators
from web_tests.pages.xpath_locators import Locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Сlick login button")
    def click_login_button(self):
        self.click_element(("xpath", LoginPageLocators.LOGIN_BUTTON))

    def mouse_over_login_button(self):
        self.mouse_over(LoginPageLocators.LOGIN_REGISTER_BTNS)





    # def perform_login(self, username, password):
    #     # TODO The test for whole Login form with username and password fields, will be implemented in future:
    #     username_locator = (By.ID, "username_input_id")
    #     password_locator = (By.ID, "password_input_id")
    #     login_button_locator = (By.ID, "login_button_id")
    #
    #     self.wait_for_element(username_locator)
    #     username_input = self.driver.find_element(*username_locator)
    #     username_input.send_keys(username)
    #
    #     self.wait_for_element(password_locator)
    #     password_input = self.driver.find_element(*password_locator)
    #     password_input.send_keys(password)
    #
    #     self.wait_for_element(login_button_locator)
    #     login_button = self.driver.find_element(*login_button_locator)
    #     login_button.click()