import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://the-internet.herokupp.com/windows")