import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import math


def func(g):
    return str(math.log(abs(12 * math.sin(int(g)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    browser.execute_script("window.scrollBy(0, 50);")
    x = int(browser.find_element(By.ID, "input_value").text)
    x = func(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert.text
    pyperclip.copy(alert.split(": ")[-1])
finally:
    browser.quit()
