import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from pages.login import LoginPage
from pages.opportunity import OpportunityPage

@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    driver.get("https://web-staging.opla-crm.com/login?redirectBack=/")
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.wait = wait
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAllApplication:

    def test_all_application(self):
        login_page = LoginPage(self.driver)
        login_page.launch_page()

        opportunities_page = OpportunityPage(self.driver)
        opportunities_page.launch_page()
        opportunities_page.get_total_products()
