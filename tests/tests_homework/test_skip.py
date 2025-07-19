"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


def test_github_desktop(setup_browser):

    if setup_browser[1] == 'Mobile':
        pytest.skip(reason='Mobile window sized')

    browser.open('https://github.com')
    browser.element('.HeaderMenu-link-wrap').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)


def test_github_mobile(setup_browser):
    if setup_browser[1] == 'Desktop':
        pytest.skip(reason='Desktop window sized')

    browser.open('https://github.com')
    browser.element('.HeaderMenu-button').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)
