import pytest
from selenium import webdriver
from utilities import read_data

import logging

Logger = logging.getLogger()


class WebDriverWrapper:
    _driver = None
    my_name = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        browser = read_data.get_read_json("data.json", "browser")
        url = read_data.get_read_json("data.json", "url")
        if browser == "ch":
            self._driver = webdriver.Chrome()
        else:
            self._driver = webdriver.Edge()

        self._driver.maximize_window()
        self._driver.implicitly_wait(30)
        self._driver.get(url)
        yield
        self._driver.quit()
