from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/wait1.html"
browser.implicitly_wait(5)

try:
    browser.get(link)
    browser.find_element(By.ID, "verify").click()
    actual = browser.find_element(By.ID, "verify_message").text
    assert "Verification was successful!" == actual
finally:
    browser.quit()
