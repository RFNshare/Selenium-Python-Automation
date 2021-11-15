# import logging
#
# logger = logging.getLogger(__name__)
#
# logger.addHandler()
# finalhandler = logging.FileHandler('logfile.log')
# logger.debug('Debug Statement is executed')
# logger.info("Information")
# logger.warning("Warning Statement")
# logger.error("A major error")
# logger.critical("Critical Issue")


from selenium import webdriver
import pytest
import time, sys
from selenium.webdriver.common.keys import Keys
from utilites.BaseClass import BaseClass


class TestSample(BaseClass):
    def test_e2e(self):
        print("Hello")
        # search_field = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        # search_field.send_keys("01601259370")
        # search_field.send_keys(Keys.ENTER)

        # msg_field = self.driver.find_element_by_xpath(
        #     '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        # msg_field.send_keys('test')
        # msg_field.send_keys(Keys.ENTER)
        #
        # # sent check
        #
        # # seen check
        # status = self.driver.find_elements_by_xpath('//span[@data-testid="msg-dblcheck"]')
        #
        # a = status[-1]
        # time.sleep(2)
        # st = a.get_attribute('aria-label')
        # print("Previous", len(st))
        # stt = st.strip()
        # print("After", len(stt))
        #
        # assert stt == "Read"

# -------------------------------------------

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

# -----------------------------------------

import pytest
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    # Getting Cached files for Auto login
    options = webdriver.ChromeOptions()
    options.add_argument(r'--user-data-dir=C:\Users\rfnsh\AppData\Local\Google\Chrome\User Data\Default')
    options.add_argument('--profile--directory=Default')

    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    driver.get('https://web.whatsapp.com/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
