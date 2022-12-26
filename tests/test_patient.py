from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.patient_dashboard_page import PatientDashboardPage
from pages.search_or_add_patient_page import SearchOrAddPatientPage


class TestPatient(WebDriverWrapper):

    def test_add_valid_patient(self):
        login_page = LoginPage(self._driver)
        login_page.enter_username("admin")
        login_page.enter_password("pass")
        login_page.select_language_by_text("English (Indian)")
        login_page.click_login()

        # login_page.login_to_system("admin","pass","English (Indian)")

        main_page = MainPage(self._driver)
        main_page.click_on_patient()
        main_page.click_on_new_search()

        sea_add_page = SearchOrAddPatientPage(self._driver)
        sea_add_page.switch_to_pat_frame()
        sea_add_page.enter_firstname("John")
        sea_add_page.enter_lastname("Wick")
        sea_add_page.enter_dob("2022-12-26")
        sea_add_page.select_gender_by_text("Male")
        sea_add_page.click_create_new_patient()

        sea_add_page.switch_to_main_html()
        sea_add_page.click_confirm_create_new_patient()

        actual_alert_text = sea_add_page.get_alert_text_and_handle_it()
        sea_add_page.close_hbd_popup()

        patient_dashboard_page = PatientDashboardPage(self._driver)
        actual_added_paitent = patient_dashboard_page.get_added_patient_name()

        assert_that(actual_alert_text).contains("Tobacco")
        assert_that(actual_added_paitent).contains("Medical Record Dashboard - John Wick")
