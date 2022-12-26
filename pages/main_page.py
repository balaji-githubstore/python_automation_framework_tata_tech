from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# add all menu under this page
from base.webdriver_keywords import WebDriverKeywords


class MainPage(WebDriverKeywords):
    __driver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def click_on_patient(self):
        super().click_element((By.XPATH, "//div[text()='Patient']"))

    def click_on_new_search(self):
        super().click_element((By.XPATH, "//div[text()='New/Search']"))
        # self.__driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

    # def click_on_new_search(self):
    #     action=ActionChains(self.__driver)
    #     action.move_to_element(self.__driver.find_element(By.XPATH, "//div[text()='New/Search']")).perform()