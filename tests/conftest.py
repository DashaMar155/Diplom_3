import pytest
from helpers.webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
