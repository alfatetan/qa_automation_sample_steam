from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

@step("Navigate to the Steam")
def start_browser(context):
    """
    Open a browser using context.URL link
    """
    context.driver.get(context.URL)
    # Add page loading checking via explicitly waiting. Checking the loading of a last section (Header)
    last_header = Wait(context.driver, 4).until(EC.presence_of_element_located((By.XPATH,'//h2[contains(text(), "Updates and Offers")]')), message = "*** ERROR: Main page does not appear!!! ***")
    if "ERROR" in last_header:
        context.LOG.append(last_header)
    

@step("Maximize browser window")
def maximize_browser(context):
    """
    Maximize the browser's window
    """
    context.driver.maximize_window()

