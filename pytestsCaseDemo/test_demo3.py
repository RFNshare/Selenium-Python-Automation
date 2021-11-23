import pytest

# mentor@rahulshettyacademy.com
@pytest.mark.usefixtures("cross")
class TestFix:

    # def test_fix(self):
    #     print("second")
    #
    # def test_fix2(self, data):
    #     print(data[0])

    def test_fix3(self, cross):
        print(cross[0])
