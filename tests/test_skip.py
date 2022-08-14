"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from qa_guru_python_1_12 import login_form

@pytest.fixture(params=[(1920, 1080), (1024, 768), (420, 768), (320, 768)])
def browser_size(request):
    return request

@pytest.fixture(scope='function', autouse=True)
def browser_settings(browser_size):
    browser.open('https://github.com/')
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.driver.set_window_size(width=width, height=height)


def test_github_desktop(browser_size):
    if browser.driver.get_window_size()["width"] < 1010:
        pytest.skip('Size for mobile version')
    login_form.login()


def test_github_mobile():
    if browser.driver.get_window_size()["width"] > 1011:
        pytest.skip('Size for desktop version')
    login_form.login()

'''
@pytest.mark.parametrize("browser_size", [(1920, 1080)], indirect=True)
@pytest.mark.parametrize("browser_size", [(320, 768)], indirect=True)
'''