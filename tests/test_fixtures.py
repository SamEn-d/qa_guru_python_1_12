"""
 pytest --co -m mobile
 pytest --co -m desktop
"""
import pytest

from qa_guru_python_1_12 import login_form
from qa_guru_python_1_12.browser_settings import desktop_browser, mobile_browser

@pytest.mark.desktop
@pytest.mark.usefixtures('desktop_browser')
def test_github_desktop(browser_size):
    login_form.login()


@pytest.mark.mobile
@pytest.mark.usefixtures('mobile_browser')
def test_github_mobile(browser_size):
    login_form.login()


