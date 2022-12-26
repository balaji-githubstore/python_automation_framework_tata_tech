from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage


class TestPatient(WebDriverWrapper):

    def test_add_valid_patient(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("admin")
        login_page.enter_password("pass")
        login_page.select_language_by_text("English (Indian)")
        login_page.click_login()

        self.driver.find_element(By.XPATH, "//div[text()='Patient']").click()
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@name='pat']"))

        self.driver.find_element(By.CSS_SELECTOR, "#form_fname").send_keys("John")
        self.driver.find_element(By.CSS_SELECTOR, "#form_lname").send_keys("Wick")
        self.driver.find_element(By.XPATH, "//input[@id='form_DOB']").send_keys("2022-12-26")
        select_gender = Select(self.driver.find_element(By.XPATH, "//select[@id='form_sex']"))
        select_gender.select_by_visible_text("Male")
        self.driver.find_element(By.XPATH, "//button[@id='create']").click()

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
        self.driver.find_element(By.XPATH, "// input[ @ value = 'Confirm Create New Patient']").click()
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.alert_is_present())

        actual_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        if len(self.driver.find_elements(By.XPATH, "//div[@class ='closeDlgIframe']")) > 0:
            self.driver.find_element(By.XPATH, "//div[@class ='closeDlgIframe']").click()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@name='pat']"))

        actual_added_paitent = self.driver.find_element(By.XPATH,
                                                        "//h2[contains(text(),'Medical Record Dashboard')]").text

        assert_that(actual_alert_text).contains("Tobacco")
        assert_that(actual_added_paitent).contains("Medical Record Dashboard - John Wick")
