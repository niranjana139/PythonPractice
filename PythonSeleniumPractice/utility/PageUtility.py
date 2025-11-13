from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageUtility:

    def select_data_with_value(self, element, value):
        """Select an option from a dropdown by visible text"""
        select = Select(element)
        select.select_by_visible_text(
            value)  # In Python, use `select_by_visible_text` instead of `selectByContainsVisibleText`
        # Return the first selected option if needed:
        return select.first_selected_option

    def click_on_element(self, element):
        """Click on a web element"""
        element.click()

    def send_data_to_element(self, element, text):
        """Send text input to a web element"""
        element.send_keys(text)

    def scroll_to_element(self, driver, element):
        """Scroll to a specific web element"""
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    def java_script_click(self, driver, locator):
        """Click on an element using JavaScript"""
        element = driver.find_element(*locator)  # `locator` is a tuple (By.X, "value")
        js = driver.execute_script("arguments[0].click();", element)
        return js

    def clear_element_data(self, element):
        """Clear the data inside an input field"""
        element.clear()
