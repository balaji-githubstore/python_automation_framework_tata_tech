from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# add all menu under this page
class MainPage:
    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def click_on_patient(self):
        self.__driver.find_element(By.XPATH, "//div[text()='Patient']").click()

    def click_on_new_search(self):
        self.__driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

    # def click_on_new_search(self):
    #     action=ActionChains(self.__driver)
    #     action.move_to_element(self.__driver.find_element(By.XPATH, "//div[text()='New/Search']")).perform()