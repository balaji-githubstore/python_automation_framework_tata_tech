from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    # private variable - accessible within the class
    __username_locator = (By.CSS_SELECTOR, "#authUser")
    __password_locator = (By.CSS_SELECTOR, "#clearPass")
    __language_locator = (By.XPATH, "//select[@name='languageChoice']")
    __login_locator = (By.ID, "login-button")
    __ack_lic_cert_locator = (By.PARTIAL_LINK_TEXT, "Acknowledgments")
    __error_locator = (By.XPATH, "//div[contains(text(),'Invalid')]")

    __driver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        print(driver)

    def enter_username(self, username):
        super().send_keys_element(self.__username_locator, username)

    def enter_password(self, password):
        super().send_keys_element(self.__password_locator, password)

    def select_language_by_text(self, language):
        super().select_dropdown_by_text(self.__language_locator, language)

    def click_login(self):
        super().click_element(self.__login_locator)

    def get_invalid_error_message(self):
        return super().get_text_element(self.__error_locator)

    def get_username_placeholder(self):
        return super().get_attribute_element(self.__username_locator, "placeholder")

    def login_to_system(self, username, password, language):
        self.enter_username(username)
        self.enter_password(password)
        self.select_language_by_text(language)
        self.click_login()

# class LoginPage:
#     # private variable - accessible within the class
#     __driver = None
#
#     def __init__(self, driver):
#         self.__driver = driver
#         print(driver)
#
#     def enter_username(self, username):
#         self.__driver.find_element(By.ID, "authUser").send_keys(username)
#
#     def enter_password(self, password):
#         self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
#
#     def select_language_by_text(self, language):
#         select_lan = Select(self.__driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
#         select_lan.select_by_visible_text(language)
#
#     def click_login(self):
#         self.__driver.find_element(By.ID, "login-button").click()
#
#     def get_invalid_error_message(self):
#         return self.__driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
#
#     def login_to_system(self, username, password, language):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.select_language_by_text(language)
#         self.click_login()
