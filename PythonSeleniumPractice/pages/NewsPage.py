from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PythonSeleniumPractice.utility.PageUtility import PageUtility


class NewsPage:
    def __init__(self, driver):
        self.driver = driver
        self.utility = PageUtility()
       # self.wait_utility = WaitUtility()
        self.driver.implicitly_wait(10)

        # Locators for elements
        #self.arrow = (By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        self.new_btn = (By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/news/add']")
        self.news_text = (By.ID, "news")
        self.save_btn = (By.XPATH, "//button[@name='create']")
        self.cancel = (By.XPATH, "//a[text()='Cancel']")
        self.search_btn = (By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.title_search = (By.XPATH, "//input[@placeholder='Title']")
        self.search_news = (By.XPATH, "//button[@name='Search']")
        self.reset_btn = (By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        self.alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        self.manage = (By.XPATH, "//h4[text()='Manage News']")
        self.search_manage_news = (By.XPATH, "//h4[text()='Search Manage News']")

    def click_new_button(self):
        newbuttonelement = self.driver.find_element(*self.new_btn)
        self.utility.click_on_element(newbuttonelement)
        return self

    def enter_news_text(self, text):
        news_text_field = self.driver.find_element(*self.news_text)
        self.utility.send_data_to_element(news_text_field, text)
        return self

    def save_new_news_text(self):
        save_button_element = self.driver.find_element(*self.save_btn)
        self.utility.click_on_element(save_button_element)
        return self

    def add_news(self, news_text_value):
        #self.utility.click_on_element(self.arrow)
        #self.driver.find_element(*self.arrow).click()

        #self.driver.find_element(*self.new_btn).click()
        self.utility.send_data_to_element(news_text_value)
       #self.driver.find_element(*self.news_text).send_keys(news_text_value)
        #self.utility.click_on_element(self.save_btn)
       # self.driver.find_element(*self.save_btn).click()
        return self
    def is_alert_displayed(self):
        try:
            return self.driver.find_element(*self.alert).is_displayed()
        except:
            return False

    def reset_page(self):
        self.driver.find_element(*self.reset_btn).click()
        return self

    def is_reset_button_displayed(self):
        return self.driver.find_element(*self.reset_btn).is_displayed()

    def is_search_button_displayed(self):
        return self.driver.find_element(*self.search_btn).is_displayed()

    def click_search_button(self):
        self.driver.find_element(*self.search_btn).click()
    def search(self, search_term):
        searchText = self.driver.find_element(*self.title_search)
        searchText.send_keys(search_term)
    def searchNews(self):
        self.driver.find_element(*self.search_news).click()

    def is_manage_news_visible(self):
        return self.driver.find_element(*self.manage).is_displayed()

    def is_search_button_visible(self):
        return self.driver.find_element(*self.search_btn).is_displayed()