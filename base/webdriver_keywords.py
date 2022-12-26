from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverKeywords:
    __driver = None
    __wait = None
    __action = None

    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 30)
        self.__action = ActionChains(driver)

    def click_element(self, locator):
        self.__wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def send_keys_element(self, locator, text):
        self.__wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def select_dropdown_by_text(self, locator, text):
        select_lan = Select(self.__wait.until(expected_conditions.visibility_of_element_located(locator)))
        select_lan.select_by_visible_text(text)

    def get_text_element(self, locator):
        return self.__wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def mouse_hover_element(self, locator):
        self.__action.move_to_element(
            self.__wait.until(expected_conditions.visibility_of_element_located(locator))).perform()


