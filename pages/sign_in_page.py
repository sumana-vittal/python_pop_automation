from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    # sign in locators
    SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1[class*='AuthHeading']")
    SIGN_IN_BTN = (By.ID, "login")

    def verify_sign_in_url(self):
        # verify sign in header message
        self.verify_partial_url("login")

    def verify_sign_in_header(self, expected_text):
        # verify sign in header message
        self.verify_partial_text(expected_text, *self.SIGN_IN_HEADER)

    def verify_sign_in_button(self, expected_text):
        # verify sign in button is present
        self.verify_partial_text(expected_text, *self.SIGN_IN_BTN)
