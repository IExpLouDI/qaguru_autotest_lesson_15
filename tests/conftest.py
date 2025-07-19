import pytest
from selene import browser


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


desktop_size = pytest.mark.parametrize("setup_browser", [(1920, 1080)], indirect=True)
mobile_size = pytest.mark.parametrize("setup_browser", [(416, 896)], indirect=True)
