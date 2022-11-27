
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    MENU_ICON = "//div//a[contains(@class, 'header__button--menu')]"
    SIDE_BAR_PANEL = "nav-menu__list"
    SIDE_BAR_LIST_OF_ELEMENTS = "//ul[@class='nav-menu__list']//li//a"
    LOGO_HOME_PAGE = ".logo_homepage"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def click_option_in_side_menu(self, optionToClick):
        hamburger_icon = self.get_menu_locator()
        hamburger_icon.click()
        self.wait.until(expected_conditions.visibility_of(self.get_side_bar_panel()))
        side_bar_list = self.get_side_bar_list_of_elemeents()

        for option in side_bar_list:
            if option.text == optionToClick:
                option.click()
                break

    def home_page_finish_loading(self):
        self.wait.until(
            expected_conditions.visibility_of(
                self.driver.find_element(By.CSS_SELECTOR, self.LOGO_HOME_PAGE)
            )
        )

    def get_menu_locator(self):
        return self.driver.find_element(By.XPATH, self.MENU_ICON)

    def get_side_bar_panel(self):
        return self.driver.find_element(By.CLASS_NAME, self.SIDE_BAR_PANEL)

    def get_side_bar_list_of_elemeents(self):
        return self.driver.find_elements(By.XPATH, self.SIDE_BAR_LIST_OF_ELEMENTS)
