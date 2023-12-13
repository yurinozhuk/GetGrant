from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_driver(browser="chrome"):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: The browser to use (options: "chrome").
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")
        return webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Please choose 'chrome'.")


def close_driver(driver):
    """
    Close the WebDriver instance.

    :param driver: The WebDriver instance to close.
    """
    driver.quit()
