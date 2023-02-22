import os
from selenium.webdriver.common.by import By


def do_login(browser, username, password):
    """Util function to execute when attempting login.

    Args:
        browser (string): browser webdriver
        username (string): username to be provided for sign-in
        password (string): password for sign-in
    """
    usr_name = browser.find_element(By.XPATH, '//*[@id="username"]')
    pass_word = browser.find_element(By.XPATH, '//*[@id="password"]')
    login = browser.find_element(By.XPATH, '//*[@id="login"]/button')

    usr_name.send_keys(username)
    pass_word.send_keys(password)
    login.click()

def do_keypress(browser, key):
    """_summary_

    Args:
        browser (_type_): _description_
        key (_type_): _description_
    """

    input_box = browser.find_element(By.ID, 'target')
    input_box.send_keys(key)

    result = browser.find_element(By.ID, 'result')
    assert result.text == "You entered: " + key

def navigate_page(browser, page):
    checkbox_elem = browser.find_element(*page)
    checkbox_elem.click()