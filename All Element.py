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

# Extracting  Text from the web page
print(driver.title)
a = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[1]")
b = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[2]")
c = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[3]")
d = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[4]")
e = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[5]")
f = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[6]")
g = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[7]")
h = driver.find_element("xpath", "(//div[@class='value ng-binding ng-scope'])[8]")
print(a.text)
print(b.text)
print(c.text)
print(d.text)
print(e.text)
print(f.text)
print(g.text)
print(h.text)

