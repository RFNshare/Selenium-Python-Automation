import time
from selenium import webdriver
from selenium.webdriver import ActionChains
chrome_options = webdriver.ChromeOptions()
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/angularpractice")
# chrome_options.add_argument(r'--user-data-dir=C:\Users\rfnsh\AppData\Local\Google\Chrome\User Data\Default')
# chrome_options.add_argument('--profile--directory=Default')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe', options=chrome_options)

# chrome options
driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)