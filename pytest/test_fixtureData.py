import pytest


@pytest.mark.usefixtures("data_load")
class TestData:
    def test_edit(self, data_load):
        print("First Name: ", data_load[0])
