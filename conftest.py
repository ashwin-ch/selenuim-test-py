import os
import pytest
from generic.config.browser_config import Test_ConfigBrowser

def pytest_addoption(parser):
    """ pytest --option variables from shell
    --browser:
        chrome= Run tests with Chrome driver.
        firefox= Run tests with Firefox driver.
        chrome-headless = Run tests with Chrome driver, headless mode.
    --env:
        dev: Run tests in dev environment (with dev data)
        test: Run tests in test environment (with test data)
        stage: Run tests in stage environment (with stage data)
    """
    parser.addoption('--browser', help='', default='chrome')
    parser.addoption('--env', action='store', default='test', help='')


def pytest_configure(config):
    os.environ["browser"] = config.getoption('browser')
    os.environ["env"] = config.getoption('env')

@pytest.fixture
def driver():
    driver = Test_ConfigBrowser().select_browser()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()