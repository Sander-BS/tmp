import pytest



@pytest.fixture
def login_page(browser):
    print("Login page")
    pass


@pytest.fixture
def user():
    print("Create user")
    return "admin", "password123"


def test_login(login_page, user):
    username, password = user
    print("Test_Simple_B_1")
    assert username == "admin"
    assert password == "password123"



def test_login_b(login_page, user):
    username, password = user
    print("Test_Simple_B_2")
    assert username == "admin"
    assert password == "password123"