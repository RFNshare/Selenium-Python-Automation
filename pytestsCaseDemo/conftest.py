import pytest


@pytest.fixture(scope="class")
def setup():
    print("Setup")
    yield
    print("last")


@pytest.fixture(scope="class")
def data():
    print("Data")
    return ["a", "b"]


@pytest.fixture(params=[("chrome", "asd"), "firefox"])
def cross(request):
    return request.param
