from driver_setup import get_driver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.password_page import PasswordPage


def test_search_and_add_to_cart():
    driver = get_driver()
    driver.get("https://adnabu-store-assignment1.myshopify.com/password")  # Replace with real URL

    try:
        print("Page title:", driver.title)
        password_page = PasswordPage(driver)
        password_page.enter_password("AdNabuQA")
        password_page.submit_password()
        home = HomePage(driver)
        results = SearchResultsPage(driver)
        product = ProductPage(driver)

        # Step 1: Search
        home.search_product("snow board")

        # Step 2: Select product
        results.click_first_product()

        # Step 3: Add to cart
        product.add_to_cart()

        # Step 4: validate cart drawer opened
        assert product.is_cart_opened()

        # Step 5 Validate correct product added
        name = product.get_product_name()
        assert "snowboard" in name.lower()
    finally:
        driver.quit()