import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    total = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    alert = browser.switch_to.alert.text
    print(alert)
finally:
    time.sleep(2)
    browser.quit()
