from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By

@step("Navigate to the Steam")
def start_browser(context):
    """
    Open a browser using context.URL link
    """
    context.driver.get(context.URL)
    # TODO: Add page loading checking via explisitly waiting

@step("Maximize browser window")
def maximize_browser(context):
    """
    Maximize the browser's window
    """
    context.driver.maximize_window()

