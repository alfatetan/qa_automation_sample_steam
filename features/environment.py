# Selenium hooks implementation
from selenium import webdriver
from datetime import datetime as dt
import re

# def before_all():
#     pass

def before_feature(context, feature):
    # Our basic URL as a constant
    context.URL = "https://store.steampowered.com/"
    # Create an empty list for logging
    context.LOG = [f"Testing report from {dt.now().strftime("%Y-%m-%d_%H:%M:%S")}",
                   f"Feature: {feature.name}"]

def before_scenario(context, scenario):
    # Activate Chrome driver
    context.driver = webdriver.Chrome()
    # Set an implicitly wait period (3 seconds)
    context.driver.implicitly_wait(3)

# def before_step(context, step):
#     pass

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
    # Close window
    context.driver.close()
    # Quit the chrome driver
    context.driver.quit()

def after_feature(context, feature):
    context.LOG.append("======== END OF TESTING REPORT ========")
    context.LOG.append(f"Feature: {feature.name}")
    # Create a name of log file
    feature_name = "_".join(re.findall('\w+', feature.name))
    filename = f'{dt.now().strftime("%Y-%m-%d_%H:%M:%S")}_{feature_name}'
    # Save log information to the file
    with open(f"./reports/{filename}", "w") as log_file:
        for line in context.LOG:
            log_file.write(line)

# def after_all():
#     pass