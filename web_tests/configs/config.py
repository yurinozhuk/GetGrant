class Config:
    """
    Config class to store global configuration settings.

    Attributes:
        BASE_URL (str): The base URL of the website to be tested.
    """
    BASE_URL = "https://getgrant.eu/"
    DEFAULT_WAIT = 10
    SELENIUM_GRID_URL = SELENIUM_GRID_URL
    SELENIUM_GRID_PORT = "4444"
