import time

def capture_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"reports/{name}_{timestamp}.png")
