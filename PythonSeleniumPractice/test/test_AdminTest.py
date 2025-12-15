import pytest
from pymsgbox import password

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.AdminPage import AdminPage
from utility.ExcelUtility import ExcelUtility
from constant import Constants, Messages

class TestAdmin:

    @pytest.mark.smoke
    def test_verify_able_to_add_user(self,driver):
        """Test to verify that a user can be added."""
        self.driver = driver
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

        home_page = login_page.click_signin_button()

        name = excelUtility.get_string_data(2, 1, Constants.HOME_PAGE)
        password = excelUtility.get_string_data( 2, 2, Constants.HOME_PAGE)
        user_type = excelUtility.get_string_data(2, 3, Constants.HOME_PAGE)

        # Click on Admin tile and perform actions to add a new user
        admin_page =home_page.click_on_tile()
        admin_page.click_new_button().add_name_method(name).add_password_method(password).select_type(user_type).click_save()

        expected_URL="https://groceryapp.uniqassosiates.com/admin/user/add"
        actual_URL =self.driver.current_url
        # Assert that the reset button is displayed
        assert expected_URL in actual_URL, Messages.USERADD_ERROR

    def test_verify_search(self, browserinstance):
        """Test to verify that a user can be searched."""

        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        # Initialize the LoginPage object
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility(Constants.file_path)
        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, Constants.LOGIN_PAGE)
        password_value = excelUtility.get_string_data(2, 2, Constants.LOGIN_PAGE)
        # Perform login actions
        login_page.enter_username(username_value).enter_password(password_value)
        home_page = login_page.click_signin_button()


        name = excelUtility.get_string_data( 2, 1, Constants.HOME_PAGE)
        password = excelUtility.get_string_data( 2, 2, Constants.HOME_PAGE)
        user_type = excelUtility.get_string_data(2, 3, Constants.HOME_PAGE)
        # Click on Admin tile and search for the user
        admin_page=home_page.click_on_tile()
        admin_page.click_search()
        admin_page.search_username(name)
        admin_page.search_user_type(user_type)
        admin_page.search_user()

        expected_URL="https://groceryapp.uniqassosiates.com/admin/user/index"
        actual_URL = self.driver.current_url
        # Assert that the search button is displayed
        assert expected_URL in actual_URL, Messages.SEARCH_USER_ERROR