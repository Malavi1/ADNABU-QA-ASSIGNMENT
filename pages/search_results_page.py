from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, "#title--7801364480090")

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)