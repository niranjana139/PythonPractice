import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from PythonSeleniumPractice.pages.AdminPage import AdminPage
from PythonSeleniumPractice.pages.BasePage import BasePage
from PythonSeleniumPractice.pages.LoginPage import LoginPage
from PythonSeleniumPractice.pages.NewsPage import NewsPage
from PythonSeleniumPractice.utility.PageUtility import PageUtility
from PythonSeleniumPractice.utility.WaitUtility import WaitUtility


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.utility = PageUtility()
        self.wait_utility = WaitUtility()

        # Define WebElement locators
        self.admin_icon = (By.XPATH, "//a[@data-toggle='dropdown']")
        self.logout_button = (By.CSS_SELECTOR, "a i.fa-power-off")
        self.admin_tile_element = (By.XPATH, "//a[contains(@class, 'small-box-footer') and @href='https://groceryapp.uniqassosiates.com/admin/list-admin']")
        self.news_tile_element = (By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        #self.contacts_tile=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-contact' and @class='small-box-footer']")


        self.driver.implicitly_wait(10)
    #element_to_be_clickable itself expects the entire tuple as a single argument,
    #and it does its own *locator unpacking internally when it calls find_element
    #So if you tried to pass *self.admin_icon,  you’d be sending two arguments to a function that expects one tuple, hence the error
    #TypeError: element_to_be_clickable() takes 1 positional argument but 2 were given
    def click_on_admin_icon(self):

        """Click on the admin icon and wait for the page to load"""
        self.wait_utility.wait_until_clickable(self.driver,self.admin_icon)
        admin_icon_element=self.find(self.admin_icon)
        self.utility.click_on_element(admin_icon_element)
        return self

    def check_logout(self):
        """Click on the logout button and return to the LoginPage"""
        logout_element=self.find(self.logout_button)
        self.utility.click_on_element(logout_element)
        return LoginPage(self.driver)

    def is_logout_displayed(self):
        """Check if the logout button is displayed"""
        try:
            logout_element = self.find(self.logout_button)
            return logout_element.is_displayed()
        except:
            return False

    def click_on_tile(self):
        """Click on the tile to navigate to Admin Page"""
       admin_tile=self.find(self.)
        self.utility.click_on_element(admin_tile)
        return AdminPage(self.driver)

    def click_on_news_tile(self):
        """Click on the news tile to navigate to Admin Page"""
        news_tile=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.news_tile_element)
        )
        self.utility.click_on_element(news_tile)
        return NewsPage(self.driver)






