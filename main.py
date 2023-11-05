from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the GeckoDriver executable
gecko_driver_path = 'path_to_geckodriver'

# Create a Firefox WebDriver instance
driver = webdriver.Firefox(executable_path=gecko_driver_path)

# Navigate to a website
driver.get('https://example.com')

# Find and interact with elements on the page
search_box = driver.find_element_by_name('q')
search_box.send_keys('Python automation')
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds (you might need to import time for this)
import time
time.sleep(5)

# Perform more actions, like clicking links, etc.

# Close the browser
driver.quit()
