from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_SINGLE_ITEM_MESSAGE = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")

    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty_message(self, expected_message):
        self.verify_text(expected_message, *self.CART_EMPTY_MESSAGE)

    def verify_single_cart_item_message(self):
        self.verify_partial_text("1 item", *self.CART_SINGLE_ITEM_MESSAGE)

    def verify_product_name(self, expected_name):
        self.verify_text(expected_name, *self.SEARCH_RESULT_TXT)
