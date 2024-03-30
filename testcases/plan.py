from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time


def clear_input(input_element):
    input_element.click()
    input_element.send_keys(Keys.CONTROL + "a")
    input_element.send_keys(Keys.DELETE)


class TestEditQuota:

    def test_edit_quota(self, driver):
        self.driver = driver
        self.driver.get("https://web-dev.opla-crm.com/quotas")
        assert "https://web-dev.opla-crm.com/quotas" in self.driver.current_url

        # Chờ cho nút chỉnh sửa quota xuất hiện
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".styled__EditButton-sc-3u75da-6"))
        )
        edit_button.click()

        # find by id: expectedKpi
        expected_kpi = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "expectedKpi"))
        )
        clear_input(expected_kpi)

        # find by id: revenue
        revenue = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "revenue"))
        )
        clear_input(revenue)

        # Chờ cho trường số lượng xuất hiện và thực hiện các thay đổi
        input_number = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[4]//input"))
        )
        clear_input(input_number)
        input_number.send_keys("666")

        # Lưu các thay đổi
        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".styled__EditButton-sc-3u75da-6"))
        )
        edit_button.click()

        # wait 2s to load page
        time.sleep(2)

        # Kiểm tra kpi sau khi chỉnh sửa
        self.driver.get("https://web-dev.opla-crm.com/quotas")
        actual_input_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[4]"))
        )
        assert actual_input_number.text == "666"