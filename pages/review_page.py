from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ReviewPage(BasePage):

    SEARCH_BTN = (By.ID, "search_button")

    def click_search(self):
        self.click(self.SEARCH_BTN)
