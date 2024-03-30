import time
from selenium.webdriver.common.by import By

class OpportunityPage:
    def __init__(self, driver):
        self.driver = driver

    def launch_page(self):
        self.driver.get("https://web-staging.opla-crm.com/opportunity")
        time.sleep(6)
        assert "https://web-staging.opla-crm.com/opportunity" in self.driver.current_url


    def get_total_products(self):
        # Sử dụng self.driver để tìm element
        total_text_element = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-total-text']")
        total_text = total_text_element.text
        print(total_text)
        return total_text

