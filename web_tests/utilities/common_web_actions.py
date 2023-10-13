from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from web_tests.pages.common_xpath_locators import LoginPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

from web_tests.utilities.logger import log


class CommonWebActions:
    def __init__(self, driver):
        self.driver = driver
        self.log = log

    def get_element(self, locator: Union[tuple, dict], wait_time: int = DEFAULT_WAIT) -> WebDriverWait:
        try:
            logging.info(f'Waiting for element: {locator}')
            element = WebDriverWait(self.driver, wait_time).until(
                expected_conditions.visibility_of_element_located(locator))
            logging.info(f'The element "{locator}" is found? {element.is_displayed()}')
            return element
        except TimeoutException as e:
            logging.error(f'Element {locator} not found within {wait_time} seconds. {e}')
            raise AssertionError(e)

    def click_element(self, locator: Union[tuple, dict]) -> None:
        try:
            element = self.get_element(locator)
            element.click()
        except Exception as e:
            logging.error(msg=f'Error: {e}')
            raise AssertionError(e)

    def wait_for_element(self, locator_type, locator_value, wait=10):
        """
        Wait for the web element with the given locator to be present and visible.

        Args:
            locator_type (str): The type of locator to be used (e.g., ID, NAME, CLASS_NAME, CSS_SELECTOR, "xpath").
            locator_value (str): The value of the locator.
            wait (int, optional): Element wait time in seconds. Defaults to 10.

        Returns:
            selenium.webdriver.remote.webelement.WebElement: The retrieved WebElement.
        """
        if isinstance(locator_value, str):
            self.log.debug("Waiting %s seconds for web element with locator: %s", wait, locator_value)
            wd_wait = WebDriverWait(self.driver, wait)
            try:
                # Convert locator_type to uppercase
                locator = (getattr(By, locator_type.upper()), locator_value)
                element = wd_wait.until(expected_conditions.presence_of_element_located(locator))
            except NoSuchElementException:
                self.log.error("Element with locator '%s: %s' not found.", locator_type, locator_value)
                raise
        return locator_value

    def execute_script(self, element, script):
        """
        Execute JavaScript on the web element.

        Args:
            element (selenium.webdriver.remote.webelement.WebElement): The element to apply the script.
            script (str): The JavaScript code to be executed on the element.
        """
        self.driver.execute_script(script, element)

    def mouse_over(self, locator_type="xpath", locator_value=None):
        """
        Simulate mouse cursor over a given web element
        :param locator_type: str - locator type (e.g., "XPATH", "ID", "CSS_SELECTOR")
        :param locator_value: str - web element locator value
        """

        # Check if locator_value is provided, if not, you should raise an error or handle it appropriately
        if locator_value is None:
            raise ValueError("locator_value must be provided")

        # Create an ActionChains object and move the mouse cursor to the specified element
        actions = ActionChains(self.driver)

        if locator_type == "xpath":
            element = self.driver.find_element("xpath", locator_value)
        elif locator_type == "ID":
            element = self.driver.find_element(locator_value)
        elif locator_type == "CSS_SELECTOR":
            element = self.driver.find_element(locator_value)
        # Add more elif blocks for other locator types as needed
        element = self.wait_for_element(locator_type, locator_value)
        actions.move_to_element(element).perform()
