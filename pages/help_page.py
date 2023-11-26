from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class HelpPage(Page):

    # locators
    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")

    def open_help_returns_page(self):
        self.open_url("https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+"
                      "Exchanges&searchQuery=")

    def select_topic(self):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_selection)
        select.select_by_value("Promotions & Coupons")

    def verify_returns_page_opened(self):
        self.wait_for_element_visible(*self.RETURNS_HEADER)

    def verify_promotions_page_opened(self):
        self.wait_for_element_visible(*self.PROMOTIONS_HEADER)

