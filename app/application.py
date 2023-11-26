from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.help_page import HelpPage
from pages.login_page import LoginPage
from pages.partner_page import PartnerPage
from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.home_page = HomePage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.login_page = LoginPage(driver)
        self.partner_page = PartnerPage(driver)
        self.help_page = HelpPage(driver)
