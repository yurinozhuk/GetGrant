from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_driver(browser="chrome", headless=True):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: The browser to use (options: "chrome").
    :param headless: Whether to run the browser in headless mode.
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("window-size=1200x600")
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Please choose 'chrome'.")


def close_driver(driver):
    """
    Close the WebDriver instance.

    :param driver: The WebDriver instance to close.
    """
    driver.quit()
