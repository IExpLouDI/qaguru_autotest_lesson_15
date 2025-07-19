"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, be
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser_desktop():
    driver_config = Options()
    driver_config.add_argument('--start-maximized')
    browser.config.driver_options = driver_config
    browser.open('https://github.com')
    yield browser
    browser.quit()


@pytest.fixture
def browser_mobile():
    browser.config.window_width = 416
    browser.config.window_height = 896
    browser.open('https://github.com')
    yield browser
    browser.quit()


def test_github_desktop(browser_desktop):
    browser.element('.HeaderMenu-link-wrap').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)


def test_github_mobile(browser_mobile):
    browser.element('.HeaderMenu-button').click()
    browser.element("//h1[contains(text(), 'Sign in to GitHub')]").should(be.present)
