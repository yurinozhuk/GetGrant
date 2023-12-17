import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(browser="chrome", headless=True):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: The browser to use (options: "chrome").
    :param headless: Whether to run the browser in headless mode.
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1200x600")

        # Додавання опцій для зберігання знімків у вигляді артефактів
        if "CI" in os.environ:
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--start-maximized")

    # Ініціалізація WebDriver
    if browser.lower() == "chrome":
        return webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Please choose 'chrome'.")


def close_driver(driver):
    """
    Close the WebDriver instance.

    :param driver: The WebDriver instance to close.
    """
    driver.quit()
