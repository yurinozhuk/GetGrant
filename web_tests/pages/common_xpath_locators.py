class LoginPageLocators:
    """Class containing locators specific to the login page."""

    # <!-- Begin main menu -->

    NAV_MAIN_MENU = "//nav[contains(@class, 'main-mnu')]"
    LOGIN_REGISTER_BTNS = NAV_MAIN_MENU + "//li[contains(@class, 'main-mnu')][2]"
    LOGIN_BUTTON = LOGIN_REGISTER_BTNS + "//li[.//a[contains(text(), 'Login')]]"
    REGISTER_BUTTON = LOGIN_REGISTER_BTNS + "//li[.//a[contains(text(), 'Register')]]"
    DEFAULT_WAIT = 10

