# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/selects1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element(By.TAG_NAME, "select").click()
#     browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# finally:
#     time.sleep(2)
#     browser.quit()
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("88")
finally:
    time.sleep(5)
    browser.quit()
