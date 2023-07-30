from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.basedrivers import BaseDrivers


class OrderPage(BaseDrivers):
    def __init__(self, driver):
        super().__init__(driver)
        # self.wait = wait
        # super().__init__(driver)
        self.driver = driver

    # locators

    ORDER_AS_GUEST = "//button[normalize-space()='Order as Guest']"
    ENTER_NAME = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    ENTER_MOBILE = "(//input[@placeholder='Enter your mobile number'])[1]"
    ADD_ADDRESS_BUTTON = "//button[normalize-space()='Add / Change Address']"
    ENTER_ADDRESS = "body > div:nth-child(14) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    SAVE_ADDRESS_BUTTON = "//button[normalize-space()='Save Address']"
    SPECIAL_INSTRUCTIONS = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(1)"

   

    def order_as_guest(self):
        return self.element_to_be_clickable(By.XPATH, self.ORDER_AS_GUEST)

    def click_order_as_guest(self):
        time.sleep(2)
        self.order_as_guest().click()

    def name(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.ENTER_NAME)

    # def enter_name(self, name):
    #     time.sleep(2)
    #     # self.name().click()
    #     name_input = self.name()
    #     name_input.send_keys(name)

    def enter_name(self, name):
        try:
            name_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.ENTER_NAME))
            )
            name_input.click()
            name_input.send_keys(name)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")

    def mobile(self):
        return self.element_to_be_clickable(By.XPATH, self.ENTER_MOBILE)

    # def enter_mobile(self, mobile):
    #     time.sleep(2)
    #     self.mobile().click()
    #     mobile_input = self.mobile()
    #     mobile_input.send_keys(mobile)

    def enter_mobile(self, mobile):
        try:
            mobile_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ENTER_MOBILE))
            )
            mobile_input.click()
            mobile_input.send_keys(mobile)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")

    def address(self):
        return self.element_to_be_clickable(By.XPATH, self.ADD_ADDRESS_BUTTON)

    def click_address(self):
        time.sleep(2)
        self.address().click()

    def enter_address(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.ENTER_ADDRESS)

    # def enter_address_field(self, address):
    #     time.sleep(2)
    #     self.enter_address().click()
    #     address_input = self.enter_address()
    #     address_input.send_keys(address)

    def enter_address_field(self, address):
        try:
            address_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.ENTER_ADDRESS))
            )
            address_input.click()
            address_input.send_keys(address)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")

    def save_address(self):
        return self.element_to_be_clickable(By.XPATH, self.SAVE_ADDRESS_BUTTON)

    def click_save_address(self):
        time.sleep(2)
        self.save_address().click()

    def special_instructions(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.SPECIAL_INSTRUCTIONS)

    # def enter_special_instructions(self, instructions):
    #     time.sleep(2)
    #     self.special_instructions().click()
    #     address_input = self.special_instructions()
    #     address_input.send_keys(instructions)

    def enter_special_instructions(self, instructions):
        try:
            instructions_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.SPECIAL_INSTRUCTIONS))
            )
            instructions_input.click()
            instructions_input.send_keys(instructions)
            time.sleep(2)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")
