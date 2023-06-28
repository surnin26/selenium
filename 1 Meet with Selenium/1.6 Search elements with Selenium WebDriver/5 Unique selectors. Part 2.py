from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "div.first_block input[class=\"form-control first\"]").send_keys("Evgen")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input[class=\"form-control second\"]").send_keys("Jackson")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input[class=\"form-control third\"]").send_keys("gungarsk@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "div.second_block input[class=\"form-control first\"]").send_keys(7564361666)
    browser.find_element(By.CSS_SELECTOR, "div.second_block input[class=\"form-control second\"]").send_keys(
        "325663, Nikolaevsk, Sverlovskaya Obl.")
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться (используем ожидание вместо time.sleep())
    waite_element = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                       '.container h1')))

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == waite_element.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
