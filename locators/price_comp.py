import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise")

search = driver.find_element_by_xpath("//input[@type='search']")
search.send_keys('ber')
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class ='product-action']/button")

for product in products:
    product.click()

driver.find_element_by_css_selector('img[alt="Cart"]').click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
prev_amount = driver.find_element_by_css_selector("span[class='discountAmt']").text
print("Previous Amount", prev_amount)
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
# driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 100)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
after_amount = driver.find_element_by_css_selector("span.discountAmt").text
print("After Amount", after_amount)
assert float(after_amount) < float(prev_amount)
# ------------------------------
time.sleep(5)
driver.close()
