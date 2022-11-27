
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.webPages.page_Base import BasePage


class ThemesPage(BasePage):

    SAVE_BUTTON = "//div[@class='set-main-footer']//a"
    THEMES_PANEL = "set-themes"
    SINGLE_THEME = "set-theme"
    ALL_THEMES = "//div[@class='set-themes__wrapper']"
    NOTIFICATION_POP_UP = "notification"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def get_title(self):
        return self.title

    def change_theme(self, themes_name):
        self.wait_for_themes_panel_to_load()
        all_themes = self.get_all_themes()
        for theme in all_themes:
            if theme.text == themes_name:
                style = self.get_current_theme(theme)
                style.click()
                self.assert_notification_pop_up_is_shown()
                if 'is-checked' not in style.get_attribute("class"):
                    raise Exception("Theme: " + themes_name + " failed to apply")
                break

    def click_save_button(self):
        button = self.get_save_button()
        button.click()
        self.assert_redirected_to_homepage()

    def get_save_button(self):
        return self.driver.find_element(By.XPATH, self.SAVE_BUTTON)

    def assert_redirected_to_homepage(self):
        super().home_page_finish_loading()

    def wait_for_themes_panel_to_load(self):
        self.wait.until(expected_conditions.visibility_of_element_located([By.CLASS_NAME, self.THEMES_PANEL]))

    def get_all_themes(self):
        return self.driver.find_elements(By.XPATH, self.ALL_THEMES)

    def get_current_theme(self, element):
        return element.find_element(By.CLASS_NAME, self.SINGLE_THEME)

    def assert_notification_pop_up_is_shown(self):
        self.wait.until(expected_conditions.visibility_of_element_located([By.CLASS_NAME, self.NOTIFICATION_POP_UP]))
