import logging
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Test_ConfigBrowser:
    def __init__(self):
        self.BROWSER = os.getenv("browser")

    def chrome_headless_capabilities(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        capabilities = options.to_capabilities()
        return capabilities

    def select_browser(self):
        browser = self.BROWSER
        driver = None
        if browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'chrome-headless':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      desired_capabilities=self.chrome_headless_capabilities())
        else:
            raise ValueError(
                f'--browser="{browser}" is not defined in conftest.py')

        logging.info(f"Setting driver with {browser}...")

        return driver