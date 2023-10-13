# GetGrant - Automation

## Installing pytest on Windows

To utilize pytest for testing your Python projects on a Windows machine, follow these steps:

1. **Open Command Prompt or Terminal**:

   Launch a command prompt or terminal window on your Windows machine.

2. **Check Python and pip Installation**:
   
   Before installing pytest, ensure that you have Python and pip installed. 
   You can verify the presence of pip by running the following command:
   ```sh 
   pip --version

3. **Install PyTest**:

   Once pip is available, install pytest by entering the following command:

   ##### "pip install pytest"

   If pip is not installed, you can download and install it from the official Python
   website: https://www.python.org/downloads/

   This command will download and install the pytest package along with its required dependencies.

4. **Verify Installation**:

   After installation, verify that pytest was installed correctly by checking its version: 
   ```sh
   pip --version

### Installing allure on Windows:
   ```sh
    $ pip install allure-pytest
    $ py.test --alluredir=%allure_result_folder% ./tests
    $ allure serve %allure_result_folder%