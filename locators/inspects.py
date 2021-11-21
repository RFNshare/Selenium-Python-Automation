import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../pytestsSelenium/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# ---------------------------------------------------------------------------- #
# driver.find_element_by_name("name").send_keys("Abdullah Al Faroque")
# driver.find_element_by_name("email").send_keys("rfnshare@gmail.com")
# driver.find_element_by_id("exampleInputPassword1").send_keys("123456")
# driver.find_element_by_id("exampleCheck1").click()
# ---------------------------------------------------------------------------- #
# driver.find_element_by_css_selector("input[name='name']").send_keys("Another Name")
# # driver.find_element_by_link_text("Shop").click()
# # driver.find_element_by_partial_link_text("op").click()
# # ---------------------------------------------------------------------------- #
# d = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# # d.select_by_index(1)
# d.select_by_visible_text("Female")

chk = driver.find_elements_by_xpath("//*[@type='checkbox']")
for i in chk:
    print(i.get_attribute('value'))
    if i.get_attribute('value') == "option2":
        i.click()
        assert i.is_selected()
radio = driver.find_elements_by_xpath("//*[@type='radio']")
radio[0].click()
time.sleep(5)
driver.close()
