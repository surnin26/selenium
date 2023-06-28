import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[type=\"text\"][name=\"firstname\"]").send_keys("Daniel")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("Bahramonov")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("uzumuluk@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "input[type=\"file\"]").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    alert = browser.switch_to.alert.text
    print(alert)
finally:
    browser.quit()
