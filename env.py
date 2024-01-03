import os
# from os import getenv
#
# from dotenv import load_dotenv
#
# project_path = os.path.abspath(os.path.dirname(__file__))
#
# if os.path.exists(os.path.join(project_path, ".env")):
#     load_dotenv(dotenv_path=os.path.join(project_path, ".env"), verbose=True)
#
#
# def get_environment(env_variable):
#     env_var = getenv(env_variable)
#     return env_var


from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')
SELENIUM_GRID_URL = os.getenv("SELENIUM_GRID_URL")
SELENIUM_GRID_PORT = os.getenv("SELENIUM_GRID_PORT")
REMOTE = os.getenv("REMOTE") or True
