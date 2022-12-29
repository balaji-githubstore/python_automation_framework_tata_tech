import pytest
from selenium import webdriver

import logging

Logger = logging.getLogger()


class WebDriverWrapper:
    _driver = None
    my_name = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.implicitly_wait(30)
        self._driver.get("https://demo.openemr.io/b/openemr")
        yield
        self._driver.quit()
