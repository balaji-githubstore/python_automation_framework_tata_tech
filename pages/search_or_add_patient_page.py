from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SearchOrAddPatientPage:
    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def switch_to_pat_frame(self):
        self.__driver.switch_to.frame(self.__driver.find_element(By.XPATH, "//iframe[@name='pat']"))

    def enter_firstname(self,firstname):
        # self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@name='pat']"))
        self.__driver.find_element(By.CSS_SELECTOR, "#form_fname").send_keys(firstname)

    def enter_lastname(self,lastname):
        self.__driver.find_element(By.CSS_SELECTOR, "#form_lname").send_keys(lastname)

    def enter_dob(self,dob):
        self.__driver.find_element(By.XPATH, "//input[@id='form_DOB']").send_keys(dob)

    def select_gender_by_text(self,text):
        select_gender = Select(self.__driver.find_element(By.XPATH, "//select[@id='form_sex']"))
        select_gender.select_by_visible_text(text)

    def click_create_new_patient(self):
        self.__driver.find_element(By.XPATH, "//button[@id='create']").click()

    def switch_to_main_html(self):
        self.__driver.switch_to.default_content()

    def close_hbd_popup(self):
        if len(self.__driver.find_elements(By.XPATH, "//div[@class ='closeDlgIframe']")) > 0:
            self.__driver.find_element(By.XPATH, "//div[@class ='closeDlgIframe']").click()

    def click_confirm_create_new_patient(self):
        self.__driver.switch_to.frame(self.__driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
        self.__driver.find_element(By.XPATH, "// input[ @ value = 'Confirm Create New Patient']").click()
        self.__driver.switch_to.default_content()

    def get_alert_text_and_handle_it(self):
        wait = WebDriverWait(self.__driver, 30)
        wait.until(expected_conditions.alert_is_present())
        actual_alert_text = self.__driver.switch_to.alert.text
        self.__driver.switch_to.alert.accept()
        return actual_alert_text
