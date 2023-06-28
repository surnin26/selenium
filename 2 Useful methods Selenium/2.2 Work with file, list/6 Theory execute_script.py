import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://google.com/")
    browser.execute_script("document.title=\"Script\"; alert(\"Robots at work\");")
finally:
    time.sleep(2)
    browser.quit()
