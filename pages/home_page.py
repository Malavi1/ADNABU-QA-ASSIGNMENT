from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    ICON_SEARCH = (By.XPATH, "//summary[contains(@aria-label,'Search')]")    
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search__button.field__button")

    def search_product(self, product_name):
        self.click(self.ICON_SEARCH)
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)