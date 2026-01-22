#generate a python selenium test script to login to https://example.com with valid and invalid credentials using pytest.Use excel file to read the test data.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utility.ExcelUtility import ExcelUtility
from constant import Constants
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()  # or any other browser driver
        self.driver.maximize_window()
        self.driver.get("https://example.com/login")

    def teardown_method(self):
        self.driver.quit()

    def test_login_valid(self):
        excel = ExcelUtility(Constants.file_path)
        username_value = excel.get_string_data(2, 1, "LoginPage")
        password_value = excel.get_string_data(2, 2, "LoginPage")

        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        home_page = login_page.click_signin_button()

        assert self.driver.current_url == "https://example.com/dashboard"

    @pytest.mark.parametrize("row", [3, 4])
    def test_login_invalid(self, row):
        excel = ExcelUtility(Constants.file_path)
        username_value = excel.get_string_data(row, 1, "LoginPage")
        password_value = excel.get_string_data(row, 2, "LoginPage")

        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()

        assert self.driver.current_url != "https://example.com/dashboard"
        print("INVALID login attempt URL:", self.driver.current_url)