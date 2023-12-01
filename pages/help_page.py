from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger


class HelpPage(Page):

    # locators
    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    GIFTCARD_HEADER = (By.XPATH, "//h1[text()=' Target GiftCard balance']")

    def open_help_returns_page(self):
        self.open_url("https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+"
                      "Exchanges&searchQuery=")

    def select_topic(self, select_topic):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        logger.info(f'selecting from {select_topic} drop-down')
        select = Select(topic_selection)
        select.select_by_value(select_topic)

    def verify_returns_page_opened(self):
        self.wait_for_element_visible(*self.RETURNS_HEADER)

    def verify_promotions_page_opened(self):
        self.wait_for_element_visible(*self.PROMOTIONS_HEADER)

    def verify_selected_topic_header_page_opened(self, topic_header):
        #self.wait_for_element_visible(*self.GIFTCARD_HEADER)
        self.driver.find_element(By.XPATH, "//h1[text()=' "+topic_header+"']")

