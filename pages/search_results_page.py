from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='resultsHeading']")

    def verify_search_result_header(self, product):
        search_result_header = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert product in search_result_header, f"Expected text {product} not in  {search_result_header}"

    def verify_search_result_url(self, expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f"Expected text {expected_keyword} not in  {self.driver.current_url}"

