from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class LoginPage(Page):

    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[class*='SignInButton']")
    SIGN_IN_FORM = (By.CSS_SELECTOR, "[class*='AuthContainerWrapper']")
    TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")
    INVALID_ACCOUNT_MESSAGE = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")

    def input_user_email_password(self, username, password):
        self.input(username, *self.EMAIL_FIELD)
        self.input(password, *self.PASSWORD_FIELD)

    def click_sign_in_button(self):
        self.wait_for_element_click(*self.SIGN_IN_BTN)
        #sleep(5)

    def click_terms_and_conditions(self):
        self.wait_for_element_click(*self.TERMS_AND_CONDITIONS)

    def verify_user_successfully_logged_in(self):
        self.wait_for_element_disappear(*self.SIGN_IN_FORM)

    def verify_invalid_account_message(self):
        self.wait_for_element_disappear(*self.INVALID_ACCOUNT_MESSAGE)

