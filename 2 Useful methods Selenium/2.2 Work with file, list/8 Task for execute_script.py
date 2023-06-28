import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


"""Тут нужно подумать, как подправить смещение вниз с помощью JS"""
try:
    browser.get(link)
    browser.maximize_window()
    x = int(browser.find_element(By.ID, "input_value").text)
    x = func(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.execute_script("window.scrollBy(0, 50);")
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    alert = browser.switch_to.alert.text
    print(alert)
finally:
    time.sleep(2)
    browser.quit()
