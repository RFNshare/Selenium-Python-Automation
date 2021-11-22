def test_three():
    msg = "Hello three"
    assert "Fail" in msg, "Message didn't match"


def test_four():
    a = 5
    b = 6
    assert a+2 == 7, "Addition Match"
