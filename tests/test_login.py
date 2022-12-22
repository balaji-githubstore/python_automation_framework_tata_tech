import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that
from selenium.webdriver.support.select import Select

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self.driver.title)

    def test_app_desc(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_login_placeholder(self):
        actual_username_placeholder = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute(
            "placeholder")

        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)


class TestLogin(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,language,expected_title", data_source.test_valid_login_data)
    def test_valid_login(self, username, password, language, expected_title):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text(language)
        self.driver.find_element(By.ID, "login-button").click()
        assert_that(expected_title).is_equal_to(self.driver.title)

    def test_invalid_login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("john")
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("john123")
        select_lan = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text("Dutch")
        self.driver.find_element(By.ID, "login-button").click()
        # assert the error message - Invalid username or password
