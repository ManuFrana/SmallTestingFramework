import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.webPages.page_Base import BasePage


class AllSettings(BasePage):

    LANGUAGE_SELECT = "setting_kad"
    LANGUAGE_SELECT_OPTIONS = "//select[@id='setting_kad']//option"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def get_title(self):
        return self.title

    def change_language_to(self, new_language, assertion):
        self.wait_language_select_to_load()
        select = self.get_language_select_options()
        for language in select:
            if new_language == language.text:
                language.click()
                break
        self.assert_language_label_is_changed_to(assertion)

    def wait_language_select_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located([By.ID, self.LANGUAGE_SELECT]))

    def get_language_select_options(self):
        return self.driver.find_elements(By.XPATH, self.LANGUAGE_SELECT_OPTIONS)

    def assert_language_label_is_changed_to(self, newLabel):
        xpath_locator = "//p[@class='frm__label' and text()='" + newLabel + "']"
        self.wait.until(expected_conditions.visibility_of_element_located([By.XPATH, xpath_locator]))