import pytest
import sys
import os

from PythonSeleniumPractice.constant import Constants
from PythonSeleniumPractice.pages.LoginPage import LoginPage
from PythonSeleniumPractice.utility.ExcelUtility import ExcelUtility


class TestNewsTest:

    def test_verify_add_news(self,driver):
        self.driver = driver
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        # Add the path to the pages directory

        login_page = LoginPage(self.driver)

        excelUtility = ExcelUtility(Constants.file_path)
        excelUtility = ExcelUtility(Constants.file_path)

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")

        login_page.enter_username(username_value).enter_password(password_value)
        home_page=login_page.click_signin_button()
        news_page=home_page.click_on_news_tile()
        #news_page = NewsPage(self.driver)
        # Add News
        news_page.click_new_button().enter_news_text("New course offered").save_new_news_text()
        #news_page.add_news("New course offered")

        # Assert Alert is displayed
        assert news_page.is_alert_displayed(), "Alert is not displayed for adding news"

    @pytest.mark.smoke
    def test_verify_reset(self,driver):
        self.driver = driver
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")
        login_page.enter_username(username_value).enter_password(password_value)
        home_page=login_page.click_signin_button()
        #news_page =NewsPage(self.driver)

        # Verify Reset functionality
        news_page=home_page.click_on_news_tile().reset_page()
        is_visible = news_page.is_reset_button_displayed()
        assert is_visible, "Reset button is not visible"


    @pytest.mark.parametrize("search_term", ["New Courses Offered", "Special Discounts", "Top Selling Products"])
    def test_verify_search_news(self,driver,search_term):
        self.driver = driver
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        home_page=login_page.click_signin_button()
        news_page=home_page.click_on_news_tile()
        #news_page = NewsPage(self.driver)
        # Search News
        #news_page.click_tile()
        news_page.click_search_button()
        news_page.search(search_term)
        news_page.searchNews()
        is_displayed = news_page.is_search_button_displayed()


        # Assert Search Button is visible
        assert is_displayed, "Search button is not visible"