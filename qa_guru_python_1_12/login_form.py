import time

from selene.support.shared import browser


def login():
    if browser.driver.get_window_size()["width"] < 1010:
        browser.element('.octicon.octicon-three-bars').click()
    browser.element('[href="/login"]').click()
    time.sleep(1)