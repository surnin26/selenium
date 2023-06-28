import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def func(g):
    return str(math.log(abs(12 * math.sin(int(g)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = int(browser.find_element(By.ID, "input_value").text)
    x = func(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    alert = browser.switch_to.alert.text
    pyperclip.copy(alert.split(": ")[-1])
finally:
    browser.quit()
