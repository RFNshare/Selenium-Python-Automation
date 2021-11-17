import time

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/angularpractice")
# driver.find_element_by_css_selector("input[name='name']").send_keys("FUCK")
# driver.find_element_by_xpath('`//input[@type="submit"]').click()
# display = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
# print(display)
driver.get("https://login.salesforce.com/")
time.sleep(2)
username = driver.find_element_by_css_selector('input#username')
username.send_keys("Hallo")
password = driver.find_element_by_css_selector('input.password')
password.send_keys('123456')
time.sleep(2)
username.clear()
password.clear()
driver.find_element_by_xpath("//input[@id='Login']").click()
# driver.find_element_by_link_text('Forgot Your Password?').click()
# //label[text()='Username']
# print(driver.find_element_by_xpath("//div[@class='verifyform']/label").text)
# div[class='verifyform'] label
# xpath parent-child
# //form[@name='forgotPassword']/div[@class='verifyform']/input[@ud]
# //form[@name='forgotPassword']/div[1]/input[@id='un']

# css parent child
# form[name='login'] label[for='password']
# form[name='login'] label:nth-child(3)
time.sleep(2)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
