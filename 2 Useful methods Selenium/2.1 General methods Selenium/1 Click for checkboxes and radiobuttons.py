from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")
x_element = browser.find_element(By.ID, "input_value").text
y = calc(x_element)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, ".form-check-input[id=\"robotCheckbox\"]").click()
browser.find_element(By.CSS_SELECTOR, ".form-check-input[id=\"robotsRule\"]").click()
browser.find_element(By.TAG_NAME, "button").click()
print(browser.switch_to.alert.text)
browser.quit()