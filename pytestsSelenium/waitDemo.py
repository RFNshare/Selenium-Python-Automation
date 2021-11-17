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
lst = []
count = 0
# //div[@class = 'product-action']/button/parent::div/parent::div/h4 (Traverse child to parent)
for product in products:
    count += 1
    product_name = product.find_element_by_xpath("parent::div/parent::div/h4").text
    product.click()
    print("No-", count, product_name)
    print("Adding this product into list, loading.....")
    time.sleep(3)
    lst.append(product_name)
print(lst)

driver.find_element_by_css_selector('img[alt="Cart"]').click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
# driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
# driver.implicitly_wait(5)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
driver.close()
