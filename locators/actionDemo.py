import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice")
action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()
# action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()
# action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
alert.accept()