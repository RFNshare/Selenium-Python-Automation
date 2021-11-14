from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element_by_xpath('//*[@id="autosuggest"]').send_keys('ind')
time.sleep(2)
countries = driver.find_elements_by_css_selector('li[class="ui-menu-item"] a')
print(len(countries))
for country in countries:
    print(country.text)
    if country.text == "Indonesia":
        country.click()
        break
assert driver.find_element_by_xpath('//*[@id="autosuggest"]').get_attribute('value') == "Indonesia"