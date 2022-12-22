import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that


class TestLoginUI:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        self.driver.quit()

    def test_title(self):
        assert_that("OpenEMR Login").is_equal_to(self.driver.title)

    def test_app_desc(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")
