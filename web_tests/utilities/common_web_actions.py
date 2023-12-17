import logging
from typing import Union
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from web_tests.configs.config import Config
from web_tests.utilities.logger import log


class CommonWebActions:
    def __init__(self, driver):
        self.driver = driver
        self.log = log

    def get_element(self, locator: Union[tuple, dict], wait_time: int = Config.DEFAULT_WAIT) -> WebDriverWait:
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
                wd_wait.until(expected_conditions.presence_of_element_located(locator))
            except NoSuchElementException:
                self.log.error("Element with locator '%s: %s' not found.", locator_type, locator_value)
                raise

    def execute_script(self, element, script):
        """
        Execute JavaScript on the web element.

        Args:
            element (selenium.webdriver.remote.webelement.WebElement): The element to apply the script.
            script (str): The JavaScript code to be executed on the element.
        """
        self.driver.execute_script(script, element)

    def mouse_over(self, locator_value, locator_type="xpath"):
        """
        Simulate mouse cursor over a given web element
        :param locator_type: str - locator type (e.g., "xpath", "id", "css selector")
        :param locator_value: str - web element locator value
        """
        # Create an ActionChains object and move the mouse cursor to the specified element
        actions = ActionChains(self.driver)

        # Map the provided locator_type to the corresponding By class
        locator_type_map = {
            "xpath": By.XPATH,
            "id": By.ID,
            "css selector": By.CSS_SELECTOR,
            # Add more mappings as needed
        }

        # Use the appropriate By class for the specified locator_type
        locator_type = locator_type.lower()
        if locator_type not in locator_type_map:
            raise ValueError(f"Unsupported locator type: {locator_type}")

        # Wait for the element to be present and visible
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type_map[locator_type], locator_value))
        )

        # Move the mouse cursor to the specified element
        actions.move_to_element(element).perform()
