import pytest


@pytest.mark.smoke
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hello"


@pytest.mark.xfail
def test_greet2():
    print("evening")
