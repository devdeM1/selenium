import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            driver_fixture = None
            for name, fixture in item.funcargs.items():
                if isinstance(fixture, webdriver.Remote):
                    driver_fixture = fixture
                    break

            if driver_fixture:
                screenshot = driver_fixture.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG,
                    extension=".png"
                )
        except Exception as e:
            print(f"⚠️ Failed to capture failure details: {str(e)}")
            allure.attach(
                f"Failed to capture screenshot: {str(e)}",
                name="screenshot_failure",
                attachment_type=allure.attachment_type.TEXT
            )