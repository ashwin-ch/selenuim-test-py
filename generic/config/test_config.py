import os
from selenium.webdriver.common.by import By

class TestConfig:
    username = "tomsmith"
    password = "SuperSecretPassword!"
    incorrect_username = "tomsmith1"
    incorrect_password = "NotAPassword"
    num_of_elem = 2
    test_case_routine = 1
    default_elem = 0
    heading_checkbox = "Checkboxes"
    heading_avl_ex = "Available Examples"
    title = "The Internet"
    page_1_heading = "Welcome to the-internet"
    ab_variation = "A/B Test Variation 1"
    ab_control = "A/B Test Control"
    add_elem_title = "Add/Remove Elements"
    list_of_options = 44
    SELECTOR_AB_TESTING = (By.CSS_SELECTOR, '#content > ul > li:nth-child(1) > a')
    SELECTOR_ADD_REM_ELEMENTS = (By.CSS_SELECTOR, '#content > ul > li:nth-child(2) > a')
    SELECTOR_AUTH = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')
    SELECTOR_CHECKBOX = (By.CSS_SELECTOR, '#content > ul > li:nth-child(6) > a')
    SELECTOR_AB_TESTING = (By.CSS_SELECTOR, '#content > ul > li:nth-child(1) > a')
    SELECTOR_DRAG_DROP = (By.CSS_SELECTOR, '#content > ul > li:nth-child(10) > a')
    SELECTOR_DROPDOWN = (By.CSS_SELECTOR, '#content > ul > li:nth-child(11) > a')
    SELECTOR_AUTH = (By.CSS_SELECTOR, '#content > ul > li:nth-child(21) > a')
    SELECTOR_KEYPRESSES = (By.CSS_SELECTOR, '#content > ul > li:nth-child(31) > a')

class XPATH_Config:
    checkbox = (By.XPATH, '//*[@id="checkboxes"]/input')
    username = (By.XPATH, '//*[@id="username"]')
    password = (By.XPATH, '//*[@id="password"]')
    login = (By.XPATH, '//*[@id="login"]/button')
    elem_button = (By.XPATH, '//*[@id="content"]/div/button')
    dropdown = (By.XPATH, '//*[@id="dropdown"]/option')