import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from constant import Constants, Messages
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utility.ExcelUtility import ExcelUtility


 # Assuming you have a fixture to set up the WebDriver
class TestHomePage:

    def test_verify_whether_user_able_to_logout(self,browserinstance):
        """Test case to verify if the user is able to logout"""
       # Replace with actual URL
        self.driver=browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        # Initialize the LoginPage object
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility(Constants.file_path)
        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, Constants.LOGIN_PAGE)
        password_value = excelUtility.get_string_data(2, 2, Constants.LOGIN_PAGE)
        # Perform login actions
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        home_page=login_page.click_signin_button()

        # Performing actions
        login_page = home_page.click_on_admin_icon().check_logout()

        # Assert URL
        actual_url = self.driver.current_url
        # Verify URL after logout
        expected_url = "https://groceryapp.uniqassosiates.com/admin/login"
        assert actual_url == expected_url, Messages.LOGOUT_ERROR
