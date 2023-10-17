import os

from env import get_environment


class Config:
    """
    Config class to store global configuration settings.

    Attributes:
        BASE_URL (str): The base URL of the website to be tested.
    """
    BASE_URL = "https://getgrant.eu/"
    DEFAULT_WAIT = 10
    EMAIL = get_environment("E-mail")
    PASSWORD = get_environment("Password")



    # PASSWORD2 = get_environment("windir") or "lolololo" # якщо в нас нема відповідної змінної,
    # то візьме лололо як дефолтний параметр (для якогось параметра який не секюрний і може бути дефолтним)