from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver.exe')

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.refresh()

# input fields
name = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/div[1]/input')
name.clear()
name.send_keys("Abdullah Al Faroque")
email = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/div[2]/input')
email.send_keys('demoemail@gmail.com')
password = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
password.send_keys('123456')
# checkbox
check = driver.find_element_by_xpath('//*[@id="exampleCheck1"]')
time.sleep(2)
check.click()
# dropdown
gender = Select(driver.find_element_by_xpath('//*[@id="exampleFormControlSelect1"]'))
gender.select_by_visible_text("Female")
gender.select_by_index(0)
# radio
driver.find_element_by_xpath('//*[@id="inlineRadio1"]').click()
# gender.select_by_value("F")
# submit
driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/input').click()
# success message grab
display = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/div[2]/div').text
print(display)
assert "Success" in display
# extra locator
# driver.find_element_by_link_text('')
