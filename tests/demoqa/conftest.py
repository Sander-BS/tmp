import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_control():
    browser.config.window_width = 2560
    browser.config.window_height = 1440
    browser.config.headless = True
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()