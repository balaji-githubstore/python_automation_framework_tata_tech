import assertpy
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that
from selenium.webdriver.support.select import Select

from base import webdriver_listener
from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from utilities import data_source




class TestLoginUI(WebDriverWrapper):
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_title(self):
        webdriver_listener.Logger.info("Validating the title Of LoginPage")
        webdriver_listener.Logger.info("Current Title is " + self._driver.title)
        assert_that("OpenEMR Login").is_equal_to(self._driver.title)

    @pytest.mark.ui
    def test_app_desc(self):
        try:
            actual_desc = self._driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
            assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")
        except BaseException as error:
            webdriver_listener.Logger.error("Failure " + error)
            assertpy.fail("test_app_desc")

    @pytest.mark.ui
    def test_login_placeholder(self):
        login_page = LoginPage(self._driver)
        actual_username_placeholder = login_page.get_username_placeholder()
        actual_password_placeholder = self._driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute(
            "placeholder")

        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)


class TestLogin(WebDriverWrapper):

    @pytest.mark.smoke
    @pytest.mark.valid
    @pytest.mark.parametrize("username,password,language,expected_title",
                             data_source.test_valid_login_data_excel)
    def test_valid_login(self, username, password, language, expected_title):
        login_page = LoginPage(self._driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_language_by_text(language)
        login_page.click_login()

        assert_that(expected_title).is_equal_to(self._driver.title)

    @pytest.mark.invalid
    @pytest.mark.parametrize("username,password,language,expected_error", data_source.test_invalid_login)
    def test_invalid_login(self, username, password, language, expected_error):
        print(self._driver)
        login_page = LoginPage(self._driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_language_by_text(language)
        login_page.click_login()

        actual_error = login_page.get_invalid_error_message()
        # assert the error message - Invalid username or password
        assert_that(expected_error).is_equal_to(actual_error)
