"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from selene import be, browser

from tests.conftest import desktop_size, mobile_size


@desktop_size
def test_github_desktop(setup_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link-wrap').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)
    pass


@mobile_size
def test_github_mobile(setup_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-button').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)
