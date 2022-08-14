"""
Переопределите параметр с помощью indirect
"""
import pytest
import time
from selene.support.shared import browser



@pytest.fixture(params=[(1920, 1080), (1024, 768), (420, 768), (320, 768)])
def browser_size(request):
    return request

@pytest.fixture(scope='function', autouse=True)
def browser_settings(browser_size):
    browser.open('https://github.com/')
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.driver.set_window_size(width=width, height=height)


@pytest.mark.mobile
@pytest.mark.parametrize("browser_size", [(320, 768)], indirect=True)
def test_github_mobile(browser_size):
    browser.element('.octicon.octicon-three-bars').click()
    browser.element('[href="/login"]').click()
    time.sleep(1)

@pytest.mark.parametrize("browser_size", [(1920, 1080)], indirect=True)
def test_github_desktop(browser_size):
    browser.element('[href="/login"]').click()
    time.sleep(1)
