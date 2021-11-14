import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()

# static dropdown handling
# driver.get("https://rahulshettyacademy.com/angularpractice")
# gender = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
# gender.select_by_visible_text('Female')

driver.get("https://rahulshettyacademy.com/dropdownsPractise")

country = driver.find_element_by_xpath("//input[@id='autosuggest']")
country.send_keys('ind')
time.sleep(2)
items = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a[1]")
time.sleep(2)
print(len(items))
for i in items:
    print(i.text)
    if i.text == "India":
        i.click()
        break
assert driver.find_element_by_xpath("//input[@id='autosuggest']").get_attribute('value') == "Indi"

