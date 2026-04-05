from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PasswordPage(BasePage):

    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def submit_password(self):
        self.click(self.SUBMIT_BUTTON)