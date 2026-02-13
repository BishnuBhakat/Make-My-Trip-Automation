import json
from pages.home_page import HomePage
from pages.module_specific_page_1 import DatePage
from pages.module_specific_page_2 import CityPage
from pages.review_page import ReviewPage

def test_bus_booking_flow(setup):
    driver = setup
    driver.get("https://www.makemytrip.com/")

    data = json.load(open("data/test_data.json"))

    home = HomePage(driver)
    date = DatePage(driver)
    city = CityPage(driver)
    review = ReviewPage(driver)

    home.close_popups()
    home.open_bus_module()

    date.select_date(data["travel_month"], data["travel_day"])
    city.select_from_city(data["source_city"])
    city.select_to_city(data["destination_city"])
    review.click_search()

    print("Search Clicked Successfully")
