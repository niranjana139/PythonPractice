from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonSeleniumPractice.utility.PageUtility import PageUtility
from PythonSeleniumPractice.utility.WaitUtility import WaitUtility


class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.page_utility = PageUtility()
        self.wait_utility = WaitUtility()

        # Locating elements
       # self.tile = self.driver.find_element(By.XPATH,"//a[contains(@class, 'small-box-footer') and @href='https://groceryapp.uniqassosiates.com/admin/list-admin']")
        self.new_button = (By.XPATH, "//a[@class=\"btn btn-rounded btn-danger\"]")
        self.add_name = (By.ID, "username")
        self.add_password =(By.ID, "password")
        self.user_type =(By.XPATH, "//select[@name='ut']")
        self.save_btn = (By.XPATH, "//button[@name='Create']")
        self.user_types = (By.XPATH, "//select[@id='user_type']")
        self.search = (By.XPATH, "//a[@class=\"btn btn-rounded btn-primary\"]")
        self.username = (By.ID, "un")
        self.user_type_drop = (By.ID, "ut")
        self.search_btn =(By.XPATH, "//button[@name='Search']")
        self.reset_btn = (By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        self.pushmenu=(By.XPATH,"//a[@data-widget='pushmenu']")
        # Implicit wait
        self.driver.implicitly_wait(10)

    def click_new_button(self):
        newButtonElement = self.driver.find_element(*self.new_button)
        self.page_utility.click_on_element(newButtonElement)
        return self

    def add_name_method(self, name):
        addnameElement = self.driver.find_element(*self.add_name)
        self.page_utility.send_data_to_element(addnameElement, name)
        return self

    def add_password_method(self, password):
        addpasswordElement = self.driver.find_element(*self.add_password)
        self.page_utility.send_data_to_element(addpasswordElement, password)
        return self

    def select_type(self, user_type_value):
        usertypeElement = self.driver.find_element(*self.user_types)
        self.page_utility.select_data_with_value(usertypeElement, user_type_value)
        return self

    def click_save(self):
        saveButtonElement = self.driver.find_element(*self.save_btn)
        self.page_utility.click_on_element(saveButtonElement)
        return self

    def is_save_Displayed(self):
        return self.save_btn.is_displayed()

    def click_search(self):
        searchbtn=self.driver.find_element(*self.search)
        self.page_utility.click_on_element(searchbtn)
        return self

    def search_username(self, name):
        searchusernameElement = self.driver.find_element(*self.username)
        self.page_utility.send_data_to_element(searchusernameElement, name)
        return self

    def search_user_type(self, user_type_value):
        searchusertypeElement = self.driver.find_element(*self.user_type_drop)
        self.page_utility.select_data_with_value(searchusertypeElement, user_type_value)
        return AdminPage(self.driver)

    def search_user(self):
        # Wait until the search button is clickable and then click
        searchbtnElement=self.driver.find_element(*self.search_btn)
        #self.wait_utility.wait_until_clickable(self.driver, self.search_btn)
        self.page_utility.click_on_element(searchbtnElement)
        return self

    def is_search_button_displayed(self):
        return self.search_btn.is_displayed()

    def is_reset_button_displayed(self):
        return self.reset_btn.is_displayed()

    def reset(self):
        resetbtnElement=self.driver.find_element(*self.reset_btn)
        self.page_utility.click_on_element(resetbtnElement)
        return AdminPage(self.driver)