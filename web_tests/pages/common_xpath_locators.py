class LoginPageLocators:
    """Class containing locators specific to the login page."""

    # <!-- Main menu -->
    NAV_MAIN_MENU = "//nav[contains(@class, 'main-mnu')]"
    LOGIN_REGISTER_BTNS = NAV_MAIN_MENU + "//li[contains(@class, 'main-mnu')][2]"
    LOGIN_BUTTON = LOGIN_REGISTER_BTNS + "//li[.//a[contains(text(), 'Login')]]"
    REGISTER_BUTTON = LOGIN_REGISTER_BTNS + "//li[.//a[contains(text(), 'Register')]]"
    HOVER_ON_SELECTOR_LANGUAGE = NAV_MAIN_MENU + "//li[contains(@class, 'main-mnu')][3]"
    SELECT_LANGUAGE = HOVER_ON_SELECTOR_LANGUAGE + "//li[1]"

    # <!-- Sign-in page -->
    SIGN_IN_FORM = "//div[contains(@class, 'form-field')]"
    EMAIL_INPUT = SIGN_IN_FORM + "//input[contains(@name, 'sign-in-email')]"
    PASSWORD_INPUT = SIGN_IN_FORM + ("//input[contains(@class, 'form-field-input') "
                                     "and contains(@autocomplete, 'new-password')]")
    SIGN_IN_BUTTON = "(//button[contains(@type, 'submit')])[1]"

    # <!-- Private page -->
    PRIVATE_CONTAINER = "//div[contains(@class, 'private__container')]"
