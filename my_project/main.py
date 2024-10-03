import time

import pandas as pd
import undetected_chromedriver as uc  # Use version 3 of undetected-chromedriver
from selenium.webdriver.common.keys import Keys

# Selenium Grid Hub URL
hub_url = 'http://selenium-hub:4444/wd/hub'

# Set up Chrome options
chrome_options = uc.ChromeOptions()

# Create a remote WebDriver instance with undetected-chromedriver
driver = uc.Chrome(
    version_main=96,  # Adjust this to the correct version of Chrome on your node if needed
    command_executor=hub_url,
    options=chrome_options
)

try:
    # Open Google
    driver.get('https://www.google.com')
    time.sleep(100)
    # Find the search box and perform a search
    search_box = driver.find_element("name", 'q')
    search_box.send_keys('Selenium Grid with Docker')
    search_box.send_keys(Keys.RETURN)
    #hello
    #Added
    # Click the first result link
    first_result = driver.find_element("xpath", '(//h3)[1]')
    first_result.click()

finally:
    # Quit the driver after the test is done
    driver.quit()
