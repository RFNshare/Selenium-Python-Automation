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

products = driver.find_elements_by_xpath("//tr/td[5]/p")
cart_sum = 0
for product in products:
    print(product.text)
    cart_sum += float(product.text)


print(cart_sum)

after_sum = driver.find_element_by_css_selector("span.totAmt").text
print(float(after_sum))

assert cart_sum == float(after_sum)



# ------------------------------
time.sleep(5)
driver.close()