
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.webPages.page_Base import BasePage


class Search(BasePage):
    INPUT_FIELD_LOCATOR = "search_form_input_homepage"
    SEARCH_BUTTON = "search_button_homepage"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def get_title(self):
        return self.title

    """
    Searches some search_string in the webPage and waits until title matches with the search_string searched
    """
    def search(self, search_string):
        input_bar = self.driver.find_element(By.ID, "search_form_input_homepage")
        input_bar.click()
        input_bar.send_keys(search_string)
        search_button = self.driver.find_element(By.ID, "search_button_homepage")
        search_button.click()
        self.wait.until(expected_conditions.title_is(search_string + " at DuckDuckGo"))

    def get_search_input_field(self):
        return self.driver.find_element(By.ID, self.INPUT_FIELD_LOCATOR)

    def get_search_icon(self):
        return self.driver.find_element(By.ID, self.SEARCH_BUTTON)
