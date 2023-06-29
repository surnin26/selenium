from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

browser = webdriver.Chrome()
link_registration_with_all_field = "http://suninjuly.github.io/registration1.html"
link_registration_with_not_all_field = "http://suninjuly.github.io/registration2.html"
browser.implicitly_wait(10)
expected_result = "Congratulations! You have successfully registered!"


class TestsRegistrationNewUser(unittest.TestCase):
    def test_registration_with_all_field(self):
        try:
            browser.get(link_registration_with_all_field)
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control first\"]") \
                .send_keys("Daniel")
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control second\"]") \
                .send_keys("Surnin")
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control third\"]") \
                .send_keys("cyrnin@gmail.com")
            browser.find_element(By.CSS_SELECTOR, ".second_block input[class=\"form-control first\"]") \
                .send_keys("+7 (799) 656-25-58")
            browser.find_element(By.CSS_SELECTOR, ".second_block input[class=\"form-control second\"]") \
                .send_keys("Smolensk, Gagarina street, 79")
            browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
            actual_result = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(actual_result, expected_result, f"Actual result text {actual_result}"
                                                             f" is not equal expected_result {expected_result}")
        finally:
            browser.quit()

    def test_registration_with_not_all_field(self):
        try:
            browser.get(link_registration_with_not_all_field)
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control first\"]") \
                .send_keys("Daniel")
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control second\"]") \
                .send_keys("Surnin")
            browser.find_element(By.CSS_SELECTOR, ".first_block input[class=\"form-control third\"]") \
                .send_keys("cyrnin@gmail.com")
            browser.find_element(By.CSS_SELECTOR, ".second_block input[class=\"form-control first\"]") \
                .send_keys("+7 (799) 656-25-58")
            browser.find_element(By.CSS_SELECTOR, ".second_block input[class=\"form-control second\"]") \
                .send_keys("Smolensk, Gagarina street, 79")
            browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
            actual_result = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(actual_result, expected_result, f"Actual result text {actual_result}"
                                                             f" is not equal expected_result {expected_result}")
        finally:
            browser.quit()
