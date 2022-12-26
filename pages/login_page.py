from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    # private variable - accessible within the class
    __driver = None

    def __init__(self, driver):
        self.__driver = driver
        print(driver)

    def enter_username(self, username):
        self.__driver.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    def select_language_by_text(self, language):
        select_lan = Select(self.__driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text(language)

    def click_login(self):
        self.__driver.find_element(By.ID, "login-button").click()

    def get_invalid_error_message(self):
        return self.__driver.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text

    def login_to_system(self, username, password, language):
        self.enter_username(username)
        self.enter_password(password)
        self.select_language_by_text(language)
        self.click_login()
