import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//h4[@class='card-title']/a")
for product in products:
    print(product.text)
    if product.text == "Blackberry":
        product.find_element_by_xpath("parent::h4/parent::div/parent::div/div[2]/button").click()
        time.sleep(5)

