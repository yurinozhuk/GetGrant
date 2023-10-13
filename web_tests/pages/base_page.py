import logging

from selenium.webdriver.support.ui import WebDriverWait

from web_tests.configs.config import Config
from web_tests.utilities.common_web_actions import CommonWebActions


class BasePage(CommonWebActions):
    """
    BasePage class representing a base page for other page classes.

    Attributes:
        driver: The WebDriver instance.
        wait: WebDriverWait object for explicit waits.
    """

    # Configure logging settings
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    def __init__(self, driver):
        """
        Initialize the BasePage with the driver and WebDriverWait.

        :param driver: The WebDriver instance.
        """
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = logging.getLogger(__name__)

        # Maximize the browser window to the full screen width
        self.driver.maximize_window()

    def navigate_to_base_url(self):
        """Navigate to the base URL specified in the Config class."""
        self.driver.get(Config.BASE_URL)
        self.log.info("Navigated to the base URL: %s", Config.BASE_URL)
