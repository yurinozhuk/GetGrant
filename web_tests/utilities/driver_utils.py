from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_driver(browser="chrome", headless=False):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: The browser to use (options: "chrome").
    :param headless: Whether to run the browser in headless mode.
    :return: The WebDriver instance (e.g., ChromeDriver).
    :raises ValueError: If an unsupported browser is provided.
    """
    # if browser.lower() == "chrome":
    #     chrome_options = ChromeOptions()
    #     if headless:
    #         chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--start-maximized")
    #     return webdriver.Chrome(options=chrome_options)

    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options = FirefoxOptions()
        chrome_options.add_argument("--start-maximized")

        return webdriver.Remote(
            command_executor='http:selenium-hub:4444/wd/hub',
            # command_executor='http://127.0.0.1:4444/wd/hub',
            options=chrome_options)

        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("window-size=1920x1080")
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
