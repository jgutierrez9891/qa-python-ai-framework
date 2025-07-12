import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver
    #browser_name = request.config.getoption( "browser_name" )
    browser_name = os.environ["BROWSER"]
    #service_obj = Service()
    chrome_service = ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    browser_options = Options()
    options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
    ]
    for option in options:
        browser_options.add_argument(option)

    if browser_name == "chrome":
        #driver = webdriver.Chrome( service=service_obj )
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=browser_options)
    elif browser_name == "firefox":
        #driver = webdriver.Firefox( service=service_obj )
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "chromium":
        driver = webdriver.Chrome(service=chrome_service,options=browser_options)

    driver.implicitly_wait( 5 )
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution
    driver.close()  #post your test function execution


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed or not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            #_capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
