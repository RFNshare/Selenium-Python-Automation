import pytest


@pytest.fixture(scope="class")
def setup():
    print('setup')
    yield
    print("setup lastdfs")


@pytest.fixture(scope="class")
def data_load():
    print("Profile Data")
    return ["Abdullah Al", "Faroque", "rfnshare@gmail.com"]


@pytest.fixture(params=[('Chrome',"Raju"), 'Firefox'])
def cross_browser(request):
    print("Cross Browser Profile Data")
    return request.param