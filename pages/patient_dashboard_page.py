from selenium.webdriver.common.by import By


class PatientDashboardPage:
    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def get_added_patient_name(self):
        self.__driver.switch_to.frame(self.__driver.find_element(By.XPATH, "//iframe[@name='pat']"))

        actual_added_paitent = self.__driver.find_element(By.XPATH,
                                                        "//h2[contains(text(),'Medical Record Dashboard')]").text
        self.__driver.switch_to.default_content()
        return actual_added_paitent
