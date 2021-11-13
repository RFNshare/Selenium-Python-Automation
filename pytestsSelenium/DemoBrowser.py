from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
# driver = webdriver.Firefox(
#     executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\geckodriver.exe')
# driver = webdriver.Edge(
#     executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\msedgedriver.exe')
# driver.maximize_window()
# driver.get("https://rfnshare.github.io")
# print(driver.title)
# print(driver.current_url)
# driver.get("https://www.fiverr.com/rfnshare")
# driver.back()

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.refresh()
name = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/div[1]/input')
name.send_keys("Abdullah Al Faroque")

# driver.minimize_window()

# driver.close()  # current window close
# driver_c.quit()  # all window close
