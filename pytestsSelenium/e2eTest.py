import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

checkout = driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
checkout.click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_xpath("//input[@id='country']").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='suggestions']")))

driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@value='Purchase']").click()

success = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(success)

assert "Success!" in success
driver.get_screenshot_as_file("Screenshot.png")
