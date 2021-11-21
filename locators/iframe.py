import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\rfnsh\PycharmProjects\PythonTestingUdemy\pytestsSelenium\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
main = driver.current_window_handle
frame = driver.find_element_by_xpath("//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(frame)
time.sleep(2)
driver.find_element_by_css_selector("body[id='tinymce']").clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("ASD")
driver.switch_to.window(main)
print(driver.find_element_by_tag_name("h3").text)
