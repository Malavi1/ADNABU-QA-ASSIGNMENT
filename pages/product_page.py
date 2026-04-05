from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (By.NAME, "add")
    CART_DRAWER = (By.CSS_SELECTOR, ".drawer__inner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".cart-item__name")

    def add_to_cart(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def is_cart_opened(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CART_DRAWER))
            return True
        except:
            return False

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)