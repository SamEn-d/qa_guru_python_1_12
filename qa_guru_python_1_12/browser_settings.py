import pytest
from selene.support.shared import browser

url = 'https://github.com/'

@pytest.fixture(scope='session')
def mobile_browser():
    browser.open(url)
    browser.driver.set_window_size(width=320, height=760)
    yield
    browser.quit()

@pytest.fixture(scope='session')
def desktop_browser():
    browser.open(url)
    browser.driver.set_window_size(width=1920, height=1080)
    yield
    browser.quit()

