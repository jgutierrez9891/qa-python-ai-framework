# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# you can mark (tag) tests with @pytest.mark.name and then run with -m name
# you can skip tests with @pytest.mark.skip
# fixtures are used as setup and tear down methods for test cases
# conftest file is used to generalize fixtures and make it available to all test case files

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_secondProgram(setup):
    print("Hello again")

@pytest.mark.skip
def test_firstAssert():
    msg = "Hello"
    assert msg == "Hi"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)