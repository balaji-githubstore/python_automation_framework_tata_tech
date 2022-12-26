import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that
from selenium.webdriver.support.select import Select

from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from utilities import data_source


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self._driver.title)

    def test_app_desc(self):
        actual_desc = self._driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_login_placeholder(self):
        actual_username_placeholder = self._driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        actual_password_placeholder = self._driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute(
            "placeholder")

        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)


class TestLogin(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,language,expected_title",
                             data_source.test_valid_login_data_excel)
    def test_valid_login(self, username, password, language, expected_title):
        login_page = LoginPage(self._driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_language_by_text(language)
        login_page.click_login()

        assert_that(expected_title).is_equal_to(self.driver.title)

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
