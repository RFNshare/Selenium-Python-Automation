import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
driver.get("https://dev2.augmedix.com:8191/")
user_list = [
    'test_account_scribe_dev_25@augmedix.com',
    'test_account_scribe_dev_16@augmedix.com',
    'test_account_scribe_dev_17@augmedix.com', 'test_account_scribe_dev_18@augmedix.com',
    'test_account_scribe_dev_19@augmedix.com', 'test_account_scribe_dev_20@augmedix.com',
    'test_account_scribe_dev_21@augmedix.com', 'test_account_scribe_dev_22@augmedix.com',
    'test_account_scribe_dev_23@augmedix.com', 'test_account_scribe_dev_24@augmedix.com',
    'test_account_scribe_dev_25@augmedix.com']
common_password = 'Asdfgh1234'
email = driver.find_element_by_xpath("//input[@id='ajs-login-email']")
password = driver.find_element_by_xpath("//input[@id='ajs-login-password']")
def login():
    for i in range(len(data.user_list) + 1):
        self.clear_field_and_send_keys(email, *self.locator.email)
        self.clear_field_and_send_keys(password, *self.locator.password)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='ajs-login-submit-btn']").click()
        try:
            self.element_is_displayed(*self.locator.already_logged_in_alert)
        except Exception as e:
            print(e)
            time.sleep(5)
            self.dashboard_should_open()
            break
    print('successfully logged-In')

login()
# dashboard
driver.find_elements_by_xpath(f"//option[contains(text(),'Stg Doc2 Gd')]").click()
time.sleep(5)
driver.close()
