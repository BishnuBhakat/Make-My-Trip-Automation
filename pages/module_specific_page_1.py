import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DatePage(BasePage):

    DATE_FIELD = (By.ID, "travelDate")
    NEXT_MONTH = (By.XPATH, "//span[@aria-label='Next Month']")
    MONTH_TEXT = (By.XPATH, "//div[@class='DayPicker-Caption']/div")

    def select_date(self, month, day):
        self.click(self.DATE_FIELD)

        while True:
            current_month = self.wait.wait_for_element(self.MONTH_TEXT).text
            if month in current_month:
                break
            self.click(self.NEXT_MONTH)

        self.driver.find_element(
            By.XPATH, f"//div[@aria-label='Sat Apr {day} 2026']"
        ).click()
