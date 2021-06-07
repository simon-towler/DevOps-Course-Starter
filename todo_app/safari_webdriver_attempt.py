# don't commit this file! It's just a standalone scratch file to confirm I can run a browser with Selenium WebDriver - 18may21
import pytest # no module named pytest!
from selenium import webdriver # no module named selenium!

# Module scope re-uses the fixture 
@pytest.fixture(scope='module') 
def driver():
# path to your webdriver download
    with Safari() as driver:
        yield driver
def test_python_home(driver): driver.get("https://www.python.org")
assert driver.title == 'Welcome to Python.org'

# NOT WORKING YET!