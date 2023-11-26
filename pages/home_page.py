from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class HomePage(Page):

    # search locators
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BTN         = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    # cart locators
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    # sign in locators
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    RIGHT_NAVIGATION_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")

    def open_home_page(self):
        self.open_url('https://www.target.com')

    def search(self, search_product, *locator):
        self.input(search_product, *self.SEARCH_INPUT_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart_icon(self, *locator):
        self.wait_for_element_click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_LINK)

    def click_right_navigation_sign_in(self):
        self.click(*self.RIGHT_NAVIGATION_SIGN_IN)

    def hover_over_sigin(self):
        signin_btn = self.find_element(*self.SIGN_IN_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_btn)
        actions.perform()

    def verify_signin_arrow_appear(self):
        self.wait_for_element_visible(*self.SIGN_IN_ARROW)