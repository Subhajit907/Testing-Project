import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the login page
driver.get("https://bangalore.mammoth.io/#/workspaces/12/projects/28")
time.sleep(5)
driver.maximize_window()
driver.find_element("xpath", "//input[@id='username']").send_keys("mandalsubhajit70@gmail.com")
driver.find_element("xpath", "//input[@id='password']").send_keys("Subhajit@123")
driver.find_element("xpath", "//span[@class='mm-button--text']").click()
time.sleep(5)
driver.find_element("xpath", "//div[@class='view-name text-truncate ng-binding ng-scope']").click()
time.sleep(5)
a = driver.find_element("xpath", "//span[@class='open-btn-padding ng-scope']")

driver.find_element("xpath", "//span[@class='open-btn-padding ng-scope']").click()
time.sleep(20)

current_window_handle = driver.current_window_handle
window_handles = driver.window_handles
# Switch focus to the newly opened tab
for handle in window_handles:

    if handle != current_window_handle:
        driver.switch_to.window(handle)
        break

# Using Math Function to counting the number of columns in the table
# Find all cells in the table
table_xpath1 = "//ul[@class='list ng-scope']"
table_xpath2 = "//div[@class='value ng-binding ng-scope']"
columns_number1 = driver.find_elements("xpath", table_xpath1)
columns_number2 = driver.find_elements("xpath", table_xpath2)

# Get the number of columns
column_count1 = len(columns_number1)
column_count2 = len(columns_number2)
Sum = column_count1 + column_count2
print("Number of columns in this table:", Sum)




time.sleep(10)
driver.quit()
