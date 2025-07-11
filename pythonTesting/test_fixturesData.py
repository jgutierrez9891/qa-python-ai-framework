import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample:

    def test_editProfile(self, dataLoad):
        print(dataLoad)