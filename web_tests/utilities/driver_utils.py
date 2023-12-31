from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from web_tests.configs.config import Config


def get_driver(browser="chrome", headless=False, remote=True):
    """
    Get a WebDriver instance for the specified browser.

    :param remote:
    :param browser: The browser to use (options: "chrome").
    :param headless: Whether to run the browser in headless mode.
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    if remote == "False" and browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(options=chrome_options)

    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options = FirefoxOptions()
        chrome_options.add_argument("--start-maximized")
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("window-size=1920x1080")
        return webdriver.Remote(
            command_executor=f'http://{Config.SELENIUM_GRID_URL_}:{Config.SELENIUM_GRID_PORT}/wd/hub',
            options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Please choose 'chrome'.")


def close_driver(driver):
    """
    Close the WebDriver instance.

    :param driver: The WebDriver instance to close.
    """
    driver.quit()
