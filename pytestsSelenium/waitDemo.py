import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise")

search = driver.find_element_by_xpath("//input[@type='search']")
search.send_keys('ber')
time.sleep(4)
searched_product = driver.find_elements_by_css_selector("div[class = 'product-image'] img")
print(len(searched_product))
driver.close()