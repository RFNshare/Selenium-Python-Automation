import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").get_attribute('value'))
time.sleep(2)
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
