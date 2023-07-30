import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDrivers:
    def __init__(self, driver):
        self.driver = driver


    def scroll_down(self, pixels):
        # Scroll the page downwards using JavaScript
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def scroll_down_to_end(self):
        # Scroll the page downwards using JavaScript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)


