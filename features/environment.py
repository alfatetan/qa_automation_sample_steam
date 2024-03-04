# Selenium hooks implementation
from selenium import webdriver
from datetime import datetime as dt
import re

# def before_all():
#     pass

def before_feature(context, feature):
    context.URL = "https://store.steampowered.com/"

def before_scenario(context, scenario):
    # Activate Chrome driver
    context.driver = webdriver.Chrome()
    # Set an implicitly wait period (3 seconds)
    context.driver.implicitly_wait(3)

def before_step(context, step):
    pass

def after_step(context, step):
    # if step is filed take a screenshot
    if step.status == "failed":
        # Scroll to the element
        if context.selected_element:
            actions = ActionChains(context.driver)
            actions.move_to_element(context.selected_element).perform()

        # TODO: Make a screenshot filename
        screenshot_name = "_".join(re.findall('\w+', step.name))
        filename = f'{dt.now().strftime("%Y-%m-%d_%H:%M:%S")}_{screenshot_name}'
        
        # TODO: Save it into the report folder
        context.driver.save_screenshot(f"./reports/screenshots/{filename}")
    pass

def after_scenario(context, scenario):
    pass

def after_feature(context, feature):
    pass

# def after_all():
#     pass