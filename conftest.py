import pytest
from selene import browser

@pytest.fixture()
def open_browser():
    browser.open('https://google.com').config.driver.maximize_window()
    # browser.driver.set_window_size(1024, 768)
