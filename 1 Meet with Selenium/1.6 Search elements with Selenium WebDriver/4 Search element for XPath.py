from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("1")

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()

