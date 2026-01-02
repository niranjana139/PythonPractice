import os.path

from datetime import datetime

import allure
import pytest
from selenium import webdriver


from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import base64

import pytest_html

@pytest.fixture(scope="class")
def setup():
    print("I'll perform Fixture statements")
    yield
    print("I'll perform Fixture statements")

@pytest.fixture()
def dataLoad():
    print("User profile data is created")
    return ["Niranjana","Obsqura","niranjanaobsqura@gmail.com"]

@pytest.fixture(params=["chrome","firefox","Edge"])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[("chrome","windows"),("firefox","linux"),"Edge"])
def multiCrossBrowser(request):
    return request.param


@pytest.fixture
def browserinstance():
    driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
    yield driver
    #driver.quit()  # Ensure to quit the driver after the test

@pytest.fixture(scope="function")
def browserinstance(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
    elif browser_name=="edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def setup():
    """Fixture to setup WebDriver and navigate to the login page."""
    driver = webdriver.Chrome()  # Use the appropriate path
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    driver.maximize_window()
    yield driver
    driver.quit()

# Define a fixture for WebDriver (use the browser you prefer)
@pytest.fixture(scope='function')
def driver():
    # Example with Chrome. Adjust for your browser and driver location.
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: run in headless mode for CI
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


#Add custom command line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


REPORT_FOLDER = None

def pytest_configure(config):
    global REPORT_FOLDER
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    REPORT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reports', timestamp))
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    # Override the HTML report output path dynamically
    config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")


import os
import base64
import pytest
import allure
from pytest_html import extras as html_extras

REPORT_FOLDER = os.path.join(os.getcwd(), "reports")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs.get("browserinstance")  # your driver fixture
            if driver:
                # 1️⃣ Save screenshot on disk
                safe_name = rep.nodeid.replace("::", "_").replace("/", "_")
                screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")
                os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
                driver.save_screenshot(screenshot_path)#Stores png in reports/

                # 2️⃣ Attach screenshot to Allure report
                allure.attach.file(
                    screenshot_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

                # 3️⃣ Attach screenshot to pytest-html report
                screenshot_base64 = base64.b64encode(driver.get_screenshot_as_png()).decode("utf-8")
                extra = getattr(rep, "extra", [])
                extra.append(html_extras.png(screenshot_base64))#Attach to pytest-html
                rep.extra = extra

        except Exception as e:
            print(f"Could not take screenshot: {e}")



def is_ci():
    return os.getenv("CI") == "true"


@pytest.fixture(params=["chrome", "firefox"])
def cross_browser(request):

    if request.param == "chrome":
        options = ChromeOptions()
        if is_ci():
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()

    elif request.param == "firefox":
        options = FirefoxOptions()
        if is_ci():
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        #driver = webdriver.Firefox()

    yield driver
    driver.quit()


