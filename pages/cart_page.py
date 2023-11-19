from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_empty_message(self, expected_message):
        cart_empty_message = self.verify_text(expected_message, *self.CART_EMPTY_MESSAGE)
