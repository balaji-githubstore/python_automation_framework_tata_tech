from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:

    def __init__(self, driver):
        self.d = driver
        print(driver)
        print(self.d)

    def enter_username(self, username):
        self.d.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.d.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    def select_language_by_text(self, language):
        select_lan = Select(self.d.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_lan.select_by_visible_text(language)

    def click_login(self):
        self.d.find_element(By.ID, "login-button").click()

    def get_invalid_error_message(self):
        return self.d.find_element(By.XPATH, "//div[contains(text(),'Invalid')]").text
