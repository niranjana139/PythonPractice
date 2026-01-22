from selenium.webdriver.common.by import By

from PythonSeleniumPractice.pages.BasePage import BasePage
from PythonSeleniumPractice.utility.PageUtility import PageUtility
from PythonSeleniumPractice.utility.WaitUtility import WaitUtility


class LoginPage(BasePage):

    # -------- Locators --------
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-dark.btn-block")
    DASHBOARD = (By.XPATH, "//p[text()='Dashboard']")
    TITLE = (By.XPATH, "//b[text()='7rmart supermarket']")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_utility = PageUtility()
        self.wait_utility = WaitUtility()

    # -------- Actions --------
    def enter_username(self, username):
        username_field = self.find(self.USERNAME)
        self.page_utility.send_data_to_element(username_field, username)
        return self

    def enter_password(self, password):
        password_field = self.find(self.PASSWORD)
        self.page_utility.send_data_to_element(password_field, password)
        return self

    def click_signin_button(self):
        from PythonSeleniumPractice.pages.HomePage import HomePage
        self.wait_utility.wait_until_clickable(self.driver,self.SIGNIN_BUTTON)
        signin_button = self.find(self.SIGNIN_BUTTON)
        self.page_utility.click_on_element(signin_button)
        return HomePage(self.driver)

    # -------- State / Getters --------
    @property
    def is_dashboard_displayed(self):
        try:
            self.wait_utility.wait_for_visibility(self.DASHBOARD)
            return True
        except:
            return False

    @property
    def title_text(self):
        title_element = self.find(self.TITLE)
        return title_element.text
