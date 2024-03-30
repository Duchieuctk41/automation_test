from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def launch_page(self):
        self.driver.get("https://web-staging.opla-crm.com/login?redirectBack=/")

        # email
        element_email = WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email or username']"))
        )
        element_email.clear()
        element_email.send_keys("tenant@oplacrm.com")

        # password
        element_password = WebDriverWait(self.driver, 0).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        element_password.clear()
        element_password.send_keys("Demo@2023")

        # click keep signed in
        keep_signed_in = WebDriverWait(self.driver, 0).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']"))
        )
        # check if keep_signed_in is not selected
        if not keep_signed_in.is_selected():
            keep_signed_in.click()

        # click button login
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])"))
        )
        login_button.click()

        # wait 6s to load page
        time.sleep(6)

        # Kiểm tra URL của trang sau đăng nhập
        assert "https://web-staging.opla-crm.com" in self.driver.current_url
