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
    SELECT_BUTTON = "//button[normalize-space()='Select']"
    ADD_CHEEZYTIKKA = "//html[1]/body[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]"
    VARIATION_CHEEZYTIKKA = "/html[1]/body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    FLAVOUR_CHEEZYTIKKA = "/html[1]/body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]"
    ADD_QUANTITY_TIKKA = "// body / div[3] / div[3] / div[2] / div[1] / div[3] / div[1] / div[1] / button[2] / * [1]"
    CLICK_STARTERS = "//div[contains(text(),'Starters')]"
    ADD_CHEESESTICKS = "div[id='product-item-250732'] div button[aria-label='Add To Cart']"
    CLICK_CART = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium blink-style-vubbuv'])[1]"
    CLICK_CHECKOUT = "//button[normalize-space()='Checkout']"
    CLICK_SOMEWHAT_LOCAL = "(//button[contains(text(),'Somewhat Local')])[1]"
    CLICK_CHICKEN_TIKKA = "//div[@id='product-item-250771']//div//button[@aria-label='Add To Cart'][normalize-space()='Add To Cart']"
    VARIATION_TIKKA = "/html[1]/body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    FLAVOUR_TIKKA = "//body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]"
    ADD_TO_CART_PRODUCT = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation blink-style-dc8s3f']"
    ORDER_AS_GUEST = "//button[normalize-space()='Order as Guest']"
    ENTER_NAME = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    ENTER_MOBILE = "(//input[@placeholder='Enter your mobile number'])[1]"
    ADD_ADDRESS_BUTTON = "//button[normalize-space()='Add / Change Address']"
    ENTER_ADDRESS = "body > div:nth-child(14) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"
    SAVE_ADDRESS_BUTTON = "//button[normalize-space()='Save Address']"
    SPECIAL_INSTRUCTIONS = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > textarea:nth-child(1)"

    # location by current location
    # def get_location(self):
    #     return self.element_to_be_clickable(By.XPATH, self.SELECT_BUTTON)
    #
    # def click_selectbutton(self):
    #     self.get_location().click()
    #
    # def cheezyaddition(self):
    #     return self.element_to_be_clickable(By.XPATH, self.ADD_CHEEZYTIKKA)
    #
    # def add_products_cheezyaddition(self):
    #     time.sleep(4)
    #     self.cheezyaddition().click()
    #
    # def variation(self):
    #     return self.element_to_be_clickable(By.XPATH, self.VARIATION_CHEEZYTIKKA)
    #
    # def select_variation(self):
    #     time.sleep(2)
    #     self.variation().click()
    #
    # def flavour(self):
    #     return self.element_to_be_clickable(By.XPATH, self.FLAVOUR_CHEEZYTIKKA)
    #
    # def select_flavour(self):
    #     time.sleep(2)
    #     self.flavour().click()
    #
    # def quantity(self):
    #     return self.element_to_be_clickable(By.XPATH, self.ADD_QUANTITY_TIKKA)
    #
    # def add_quantity(self):
    #     self.quantity().click()
    #
    # def add_cheezy_tikka(self):
    #     return self.element_to_be_clickable(By.XPATH, self.ADD_TO_CART_PRODUCT)
    #
    # def click_add_cheezy_tikka(self):
    #     self.add_cheezy_tikka().click()
    #
    # def somewhat_local(self):
    #     time.sleep(10)
    #     return self.driver.find_element(By.XPATH, self.CLICK_SOMEWHAT_LOCAL)
    #
    # def click_somewhat_local(self):
    #     time.sleep(10)
    #     self.somewhat_local().click()
    #
    # def chicken_tikka(self):
    #     return self.element_to_be_clickable(By.XPATH, self.CLICK_CHICKEN_TIKKA)
    #
    # def click_chicken_tikka(self):
    #     self.chicken_tikka().click()
    #
    # def variation_chicken_tikka(self):
    #     time.sleep(2)
    #     return self.driver.find_element(By.XPATH, self.VARIATION_TIKKA)
    #
    # def click_variation_chicken_tikka(self):
    #     time.sleep(2)
    #     self.variation_chicken_tikka().click()
    #
    # def flavour_chicken_tikka(self):
    #     return self.element_to_be_clickable(By.XPATH, self.FLAVOUR_TIKKA)
    #
    # def click_flavour_chicken_tikka(self):
    #     time.sleep(2)
    #     self.flavour_chicken_tikka().click()
    #
    # def add_chicken_tikka(self):
    #     return self.element_to_be_clickable(By.XPATH, self.ADD_TO_CART_PRODUCT)
    #
    # def click_add_chicken_tikka(self):
    #     self.add_chicken_tikka().click()
    #
    # def starters(self):
    #     return self.element_to_be_clickable(By.XPATH, self.CLICK_STARTERS)
    #
    # def click_starters(self):
    #     time.sleep(2)
    #     self.starters().click()
    #
    # def cheesesticks(self):
    #     return self.element_to_be_clickable(By.CSS_SELECTOR, self.ADD_CHEESESTICKS)
    #
    # def add_cheesesticks(self):
    #     time.sleep(2)
    #     self.cheesesticks().click()
    #
    # def cart(self):
    #     return self.element_to_be_clickable(By.XPATH, self.CLICK_CART)
    #
    # def click_cart(self):
    #     time.sleep(2)
    #     self.cart().click()
    #
    # def checkout(self):
    #     return self.element_to_be_clickable(By.XPATH, self.CLICK_CHECKOUT)
    #
    # def click_checkout(self):
    #     time.sleep(2)
    #     self.checkout().click()

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