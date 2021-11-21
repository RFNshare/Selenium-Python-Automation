import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

search = driver.find_element_by_xpath("//input[@type='search']")
search.send_keys('ber')
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class ='product-action']/button")
lst = []
for product in products:
    a = product.find_element_by_xpath("parent::div/parent::div/h4").text
    lst.append(a)

print(lst)
