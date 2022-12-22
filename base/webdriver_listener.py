import pytest
from selenium import webdriver


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        self.driver.quit()
