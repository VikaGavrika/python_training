
import pytest
from fixtura.application import Application

@pytest.fixture(scope="class")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture