from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class HomePage(Page):

    # locators
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BTN         = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    def open_home_page(self):
        self.open_url('https://www.target.com')

    def search(self, *locator):
        self.input('coffee', *self.SEARCH_INPUT_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)





