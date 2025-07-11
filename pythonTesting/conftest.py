import pytest

@pytest.fixture(scope="class")
def setup():
    print("Configuring tests...")
    yield
    print("Terminating tests...")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["John","Gutierrez","prueba@correo.com"]

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    print("user profile data is being created")
    return request.params