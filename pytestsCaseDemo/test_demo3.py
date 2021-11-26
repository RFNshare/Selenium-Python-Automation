import logging
import pytest

from pytestsCaseDemo.base import Base


# mentor@rahulshettyacademy.com

class TestFix(Base):

    # def test_fix(self):
    #     print("second")
    #
    # def test_fix2(self, data):
    #     print(data[0])

    def test_fix3(self, cross):
        log = self.test_Log()
        log.info(cross)
        # print(cross[0])

