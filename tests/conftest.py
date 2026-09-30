import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_control():
    browser.config.base_url = 'https://todomvc.com/examples/react/dist/'

    yield

    browser.quit()