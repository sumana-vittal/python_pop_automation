from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CirclePage(Page):

    CIRCLE_TABS = (By.CSS_SELECTOR, "a[class*='NavigationLink']")

    def open_circle(self):
        self.open_url("https://www.target.com/circle")

    def verify_circle_tabs(self):
        all_circle_tabs = self.find_elements(*self.CIRCLE_TABS)

        current_url = ''
        for i in range(len(all_circle_tabs)):
            self.find_elements(*self.CIRCLE_TABS)[i].click()
            #sleep(3)
            self.wait_for_url_to_change(current_url)
            current_url = self.driver.current_url
