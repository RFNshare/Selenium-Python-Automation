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
time.sleep(2)
shopButton = driver.find_element_by_css_selector("a[href*='shop")
driver.execute_script("arguments[0].click();", shopButton)
time.sleep(1)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
