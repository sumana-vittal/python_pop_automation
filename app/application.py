from pages.base_page import Page
from pages.cart_page import CartPage
from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.home_page = HomePage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)