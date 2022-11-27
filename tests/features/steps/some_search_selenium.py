import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



@given(u'i launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driverWait = WebDriverWait(context.driver, 3)
    context.driver.maximize_window()

@when(u'open duckduckgo main page')
def step_impl(context):
    context.driver.get("https://duckduckgo.com/")


@then(u'verify that main logo is loaded')
def step_impl(context):
    context.driverWait.until(
        expected_conditions.visibility_of(
            context.driver.find_element(By.CSS_SELECTOR, ".logo_homepage")
        )
    )


@then(u'search for "{search_string}")')
def step_impl(context, search_string):
    input_bar = context.driver.find_element(By.ID, "search_form_input_homepage")
    input_bar.click()
    input_bar.send_keys(search_string)
    search_button = context.driver.find_element(By.ID, "search_button_homepage")
    search_button.click()
    time.sleep(10)
    context.driverWait.until(expected_conditions.title_is(search_string + " at DuckDuckGo"))

@then(u'close browser')
def step_impl(context):
    context.driver.close()
