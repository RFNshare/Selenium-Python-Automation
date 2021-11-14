import pytest


#
# @pytest.fixture()
# def setup():
#     print('setup')
#     yield
#     print("setup last")
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_setup(self):
        print('setup ok')

    def test_setup1(self):
        print('setup ok 1')

    def test_setup2(self):
        print('setup ok 2')

    def test_setup3(self):
        print('setup ok 3')
