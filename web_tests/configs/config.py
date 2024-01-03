from env import SELENIUM_GRID_URL, REMOTE


class Config:
    """
    Config class to store global configuration settings.

    Attributes:
        BASE_URL (str): The base URL of the website to be tested.
    """
    BASE_URL = "https://getgrant.eu/"
    DEFAULT_WAIT = 10
    SELENIUM_GRID_URL_ = SELENIUM_GRID_URL
    SELENIUM_GRID_PORT = "4444"
    REMOTE_ = REMOTE

