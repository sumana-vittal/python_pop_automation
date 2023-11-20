from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='resultsHeading']")

    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    RIGHT_NAVIGATION_VIEW_CART = (By.CSS_SELECTOR, "a[href='/cart']")

    def verify_search_result_header(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_HEADER)

    def verify_search_result_url(self, expected_keyword):
        self.verify_partial_url(expected_keyword)

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.SEARCH_RESULT_ITEMS) # clicks on first 'add to cart'

    def click_right_navigation_view_cart(self):
        self.wait_for_element_click(*self.RIGHT_NAVIGATION_VIEW_CART)
