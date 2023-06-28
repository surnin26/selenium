import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    treasure = treasure.get_attribute("valuex")
    answer = func(treasure)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    alert = browser.switch_to.alert.text
    print(alert)

finally:
    time.sleep(2)
    browser.quit()





