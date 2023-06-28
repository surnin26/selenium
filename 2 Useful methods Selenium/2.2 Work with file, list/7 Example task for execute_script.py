import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(2)
    browser.quit()
   