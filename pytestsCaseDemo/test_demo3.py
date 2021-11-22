import pytest


@pytest.fixture()
def setup():
    print("Setup")


def test_fix(setup):
    print("second")
