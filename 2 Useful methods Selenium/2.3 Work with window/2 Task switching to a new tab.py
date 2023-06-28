import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    browser.switch_to.window(browser.window_handles[1])
    g = int(browser.find_element(By.ID, "input_value").text)
    answer = func(g)
    browser.find_element(By.CSS_SELECTOR, "input[name=\"text\"]").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button").click()
    alert = browser.switch_to.alert.text
    pyperclip.copy(alert.split(": ")[-1])
finally:
    browser.quit()
