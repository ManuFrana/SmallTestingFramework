import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Blog():

    TOP_GET_IN_TOUCH_LOCATOR = "//ul//a[text()='Get in touch']"
    BOTTOM_GET_IN_TOUCH_LOCATOR = "//article//a[text()='Get in touch']"
    INPUT_NAME_LOCATOR = "//form//input[@id='wpforms-872-field_0']"
    INPUT_EMAIL_LOCATOR = "//form//input[@id='wpforms-872-field_1']"
    INPUT_COMPANY_LOCATOR = "//form//input[@id='wpforms-872-field_6']"
    INPUT_MESSAGE_LOCATOR = "//form//textarea"
    BUTTON_SEND = "//form//button"
    SUCCESS_FORM_LOCATION = "//div[@class='box']//p[contains(@class, 'row')]"

    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.title = self.driver.title

    def get_title(self):
        return self.title

    def get_top_get_in_touch_button(self):
        return self.driver.find_element(By.XPATH, self.TOP_GET_IN_TOUCH_LOCATOR)

    def get_bottom_get_in_touch_button(self):
        return self.driver.find_element(By.XPATH, self.BOTTOM_GET_IN_TOUCH_LOCATOR)

    def fill_form(self, name='', email='', company='', message=''):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".get-in-touch-modal")))

        input_name = '' if len(name) == 0 else self.driver.find_element(By.XPATH, self.INPUT_NAME_LOCATOR)
        input_email = '' if len(email) == 0 else self.driver.find_element(By.XPATH, self.INPUT_EMAIL_LOCATOR)
        input_company = '' if len(company) == 0 else self.driver.find_element(By.XPATH, self.INPUT_COMPANY_LOCATOR)
        input_message = '' if len(message) == 0 else self.driver.find_element(By.XPATH, self.INPUT_MESSAGE_LOCATOR)

        if input_name:
            input_name.send_keys(name)
        if input_email:
            input_email.send_keys(email)
        if company:
            input_company.send_keys(company)
        if input_message:
            input_message.send_keys(message)

        # Basic form submission

        return self.driver.find_element(By.XPATH, self.BUTTON_SEND)

    def validate_form_submission(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.SUCCESS_FORM_LOCATION)))
        form = self.driver.find_elements(By.XPATH, self.SUCCESS_FORM_LOCATION)
        return form

    def validate_name_is_required(self):
        time.sleep(1)
        label = self.driver.find_element(By.XPATH, "//label[text()='This field is required.' and @id='wpforms-872-field_0-error']")
        if label:
            return True
        return False

    def validate_email_is_required(self):
        time.sleep(1)
        label = self.driver.find_element(By.XPATH, "//label[text()='This field is required.' and @id='wpforms-872-field_1-error']")
        if label:
            return True
        return False

    def validate_company_is_required(self):
        time.sleep(1)
        label = self.driver.find_element(By.XPATH, "//label[text()='This field is required.' and @id='wpforms-872-field_6-error']")
        if label:
            return True
        return False
