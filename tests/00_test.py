import os
import time
import pytest
import asyncio
# import pytest-asyncio
import logging as log   # used for printing debug statement, when test cases are failing
from selenium import webdriver # imports webdriver from selenium package
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager # Imports manager for chrome driver
from generic.config.env_config import ConfigLoader
from generic.config.test_config import TestConfig
from generic.config.test_config import XPATH_Config
import generic.util.utils as Util
import generic.util.vis as Visualize


PATH = "http://the-internet.herokuapp.com"

class Test_browser:
    @classmethod
    def setup(self, driver):
        self.config = ConfigLoader.load_config()
        self.consts = TestConfig
        self.xpath = XPATH_Config
        self.viz = Visualize

    @pytest.fixture
    @pytest.mark.asyncio
    def setup_browser(self, driver):
        log.info("Setting up browser")
        self.browser = driver
        self.browser.get(self.config.url)

    @classmethod
    def do_login(self, browser, username, password):
        usr_name = browser.find_element(*self.xpath.username)
        pass_word = browser.find_element(*self.xpath.password)
        login = browser.find_element(*self.xpath.login)

        usr_name.send_keys(username)
        pass_word.send_keys(password)
        login.click()

    @pytest.mark.asyncio
    async def test_title(self, setup_browser):
        assert self.browser.title == self.consts.title
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test_header(self, setup_browser):
        heading = self.browser.find_element(By.CLASS_NAME, "heading")
        log.debug(heading.text)
        assert heading.text == self.consts.page_1_heading

    @pytest.mark.asyncio
    async def test_header2(self, setup_browser):
        heading = self.browser.find_element(By.TAG_NAME, "h2")
        log.debug(heading.text)
        assert heading.text == self.consts.heading_avl_ex

    @pytest.mark.asyncio
    async def test_page_list(self, setup_browser):
        ## Check the list of options available in the page
        ## Test case: Check if 44 options are available in the page as a list <li>
        elements = self.browser.find_elements(By.TAG_NAME, 'li')
        assert len(elements) == self.consts.list_of_options

    @pytest.mark.asyncio
    async def test_click(self, setup_browser):
        Util.navigate_page(self.browser, self.consts.SELECTOR_AB_TESTING)
        await asyncio.sleep(1)

        element_1 = self.browser.find_element(By.TAG_NAME, "h3")
        log.debug(element_1.text)
        log.debug(self.browser.title)

        assert self.browser.title == self.consts.title

        # Test case, check the A/B variation, either it should be "Variation 1" or "Control"
        assert element_1.text == self.consts.ab_variation or element_1.text == self.consts.ab_control
        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test_add_rem_element(self, setup_browser):
        Util.navigate_page(self.browser, self.consts.SELECTOR_ADD_REM_ELEMENTS)

        await asyncio.sleep(1)
        element_1 = self.browser.find_element(By.TAG_NAME, "h3")

        # Requirement assert the page title is "the internet"
        assert self.browser.title == self.consts.title
        # ToDo: assert the page heading is "Add/Remove Elements"
        assert element_1.text == self.consts.add_elem_title

        #find the button by xpath
        button = self.browser.find_element(*self.xpath.elem_button)

        m = 0
        while m < self.consts.test_case_routine:
            m += 1
            # TC: Check if elements already exists
            elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
            assert len(elements) == self.consts.default_elem

            ## Create elements
            i = 0
            while i < self.consts.num_of_elem:
              button.click()
              i += 1
            await asyncio.sleep(1)

            # TC Check if elements are created
            elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
            assert len(elements) == self.consts.num_of_elem
            log.debug("Num of elements created %d", len(elements))

            ##delete elements
            for element in elements:
              element.click()

            # TC Check if elements are removed
            elements = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
            assert len(elements) == self.consts.default_elem

            await asyncio.sleep(1)

        self.browser.back()

        #TC: Check if we moved back to home page after back operation
        heading = self.browser.find_element(By.TAG_NAME, "h2")
        log.debug(heading.text)
        assert heading.text == self.consts.heading_avl_ex

        await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test_checkboxes(self, setup_browser):
        Util.navigate_page(self.browser, self.consts.SELECTOR_CHECKBOX)

        heading = self.browser.find_element(By.TAG_NAME, "h3")
        assert heading.text == self.consts.heading_checkbox
        log.debug("Heading for checkboxes page: %d", heading.text)

        #find checkboxes
        checkboxes = self.browser.find_elements(*self.xpath.checkbox)

        #Todo Requirement update for default page checkbox status
        # Test case: Check default state of checkboxes when page is loaded
        assert checkboxes[0].is_selected() == False
        assert checkboxes[1].is_selected() == True

        # Test case: Check all checkboxes if not selected
        for elem in checkboxes:
          if elem.is_selected() is False:
            elem.click()

        for elem in checkboxes:
          assert elem.is_selected() == True

        await asyncio.sleep(1)

        for elem in checkboxes:
          if elem.is_selected() == True:
            elem.click()

        for elem in checkboxes:
          assert elem.is_selected() == False

        await asyncio.sleep(1)

        # reload the page and check default
        self.browser.back()
        self.browser.forward()

        await asyncio.sleep(1)

        #find checkboxes
        checkboxes = self.browser.find_elements(*self.xpath.checkbox)

        #Todo Requirement update for default page checkbox status
        # Test case: Check states persists when moved back and forward
        assert checkboxes[0].is_selected() == False
        assert checkboxes[1].is_selected() == False

        await asyncio.sleep(5)

        self.browser.back()
        Util.navigate_page(self.browser, self.consts.SELECTOR_CHECKBOX)

        #find checkboxes
        checkboxes = self.browser.find_elements(*self.xpath.checkbox)

        # Test case: Check checkboxes moves to default state when the page is reloaded
        assert checkboxes[0].is_selected() == False
        assert checkboxes[1].is_selected() == True

        await asyncio.sleep(5)

    @pytest.mark.asyncio
    async def test_login_auth(self, setup_browser):
        Util.navigate_page(self.browser, self.consts.SELECTOR_AUTH)

        await asyncio.sleep(1)

        Util.do_login(self.browser, self.consts.username, self.consts.incorrect_password)
        result_flash = self.browser.find_element(By.ID, 'flash')
        assert  "Your password is invalid!" in result_flash.text
        await asyncio.sleep(1)

        Util.do_login(self.browser, self.consts.incorrect_username, self.consts.incorrect_password)
        result_flash = self.browser.find_element(By.ID, 'flash')
        assert "Your username is invalid!" in result_flash.text
        await asyncio.sleep(1)

        Util.do_login(self.browser, self.consts.username, self.consts.password)
        result_flash = self.browser.find_element(By.ID, 'flash')
        assert "You logged into a secure area!" in result_flash.text
        await asyncio.sleep(1)

        result = self.browser.find_element(By.TAG_NAME, 'h2')
        assert result.text == "Secure Area"
        await asyncio.sleep(2)

    @pytest.mark.asyncio
    async def test_dropdown(self, setup_browser):
        Util.navigate_page(self.browser, self.consts.SELECTOR_DROPDOWN)
        await asyncio.sleep(1)

        dropdown = self.browser.find_element(By.ID, "dropdown")

        select_opt = Select(dropdown)
        options = self.browser.find_elements(*self.xpath.dropdown)

        # by default option 1 is selected
        assert options[0].is_selected() == True

        select_opt.select_by_value("1")
        assert options[1].is_selected() == True

        select_opt.select_by_value("2")
        assert options[2].is_selected() == True

        select_opt.select_by_value("1")
        assert options[1].is_selected() == True

        await asyncio.sleep(2)


    @pytest.mark.asyncio
    async def test_keypress(self, setup_browser):
      Util.navigate_page(self.browser, self.consts.SELECTOR_KEYPRESSES)

      Util.do_keypress(self.browser, "1")
      Util.do_keypress(self.browser, "2")
      Util.do_keypress(self.browser, "0")
      Util.do_keypress(self.browser, "A")
      Util.do_keypress(self.browser, "B")
      Util.do_keypress(self.browser, "C")
      Util.do_keypress(self.browser, "Z")
      Util.do_keypress(self.browser, "B")

      await asyncio.sleep(1)


