import pytest
import requests

@pytest.fixture(scope="class")
def auth_user():
    token = requests.post(url='http://127.0.0.1:8080/auth', auth=("test_user", "test_pass"))
    print("We can see this text")
    return token.json()['access_token']
