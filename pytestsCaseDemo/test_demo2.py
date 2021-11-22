import pytest

@pytest.mark.skip
def test_three():
    msg = "Hello three"
    assert "Fail" in msg, "Message didn't match"


@pytest.mark.now
@pytest.mark.xfail
def test_four_credit():
    a = 5
    b = 6
    assert a + 2 == 8, "Addition didn't Match"
