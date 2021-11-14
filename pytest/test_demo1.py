import pytest


@pytest.mark.smoke
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi"


@pytest.mark.skip
def test_greet():
    print("Morning")


def test_crossbroswer(cross_browser):
    print(cross_browser)
