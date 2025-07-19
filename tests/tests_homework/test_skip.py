"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


def gen_ids(fixture_values):
    return f"width - {fixture_values[0]}, height - {fixture_values[1]}"


@pytest.fixture(params=[(1920, 1080), (416, 896)], ids=gen_ids)
def setup_browser(request):
    width, height = request.param
    window_type = 'Desktop' if width > 1000 else 'Mobile'
    browser.config.window_height = height
    browser.config.window_width = width
    yield browser, window_type
    browser.quit()


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
