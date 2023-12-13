from webbrowser import Chrome

from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_driver(browser="chrome", headless=True):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: The browser to use (options: "chrome").
    :param headless: Whether to run the browser in headless mode (default: True).
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        else:
            options.add_argument("--start-maximized")
        return Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser '{browser}'. Please choose 'chrome'.")


def close_driver(driver):
    """
    Close the WebDriver instance.

    :param driver: The WebDriver instance to close.
    """
    driver.quit()
