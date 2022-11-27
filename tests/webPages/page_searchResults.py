
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.webPages.page_Base import BasePage


class SearchResultsPage(BasePage):

    MAIN_RESULT_BLOCK_CLASS = "module__image"
    ALL_RESULTS_LOCATOR = "//article//div//h2"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def get_title(self):
        return self.title

    """
        For now let's assume that since imageContainer has an href property,
        we are seeing a relevant image for what we were searching for
    """

    def search_results_contains_image(self, input):
        image_container = self.driver.find_element(By.CLASS_NAME, "module__image")
        return image_container.get_attribute('href') is not None

    """
        Each search result is written in an "article" html tag so we use
        XPATH to search it.
    """
    def at_least_one_result_of(self, page_to_look_for):
        results = self.get_all_results()
        if (len(results) == 0):
            raise Exception("Not one result was found for " + page_to_look_for)
        return any(page_to_look_for in finding.text for finding in results)

    def get_all_results(self):
        return self.driver.find_elements(By.XPATH, self.ALL_RESULTS_LOCATOR)

    def get_main_result_block(self):
        return self.driver.find_element(By.CLASS_NAME, self.MAIN_RESULT_BLOCK_CLASS)
