from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome('./chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
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
# input fields
name = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/div[1]/input')
name.send_keys("Abdullah Al Faroque")
email = driver.find_element_by_xpath('/html/body/app-root/form-comp/div/form/div[2]/input')
email.send_keys('demoemail@gmail.com')
password = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
password.send_keys('123456')
# checkbox
check = driver.find_element_by_xpath('//*[@id="exampleCheck1"]')
time.sleep(2)
check.click()

# driver.minimize_window()
# driver.close()  # current window close
# driver_c.quit()  # all window close
