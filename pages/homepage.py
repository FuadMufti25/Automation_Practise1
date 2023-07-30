from selenium.webdriver.common.by import By
import time
from base.basedrivers import BaseDrivers

class LaunchPage(BaseDrivers):
    def __init__(self, driver):
        # super().__init__(driver)
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
    CLICK_SOMEWHAT_LOCAL = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(3)"
    CLICK_CHICKEN_TIKKA = "//div[@id='product-item-250771']//div//button[@aria-label='Add To Cart'][normalize-space()='Add To Cart']"
    VARIATION_TIKKA = "/html[1]/body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    FLAVOUR_TIKKA= "//body[1]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]"
    ADD_TO_CART_PRODUCT = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-disableElevation blink-style-dc8s3f']"
    ORDER_AS_GUEST = "//button[normalize-space()='Order as Guest']"

   


# location by current location
    def get_location(self):
        return self.element_to_be_clickable(By.XPATH, self.SELECT_BUTTON)

    def click_selectbutton(self):
        self.get_location().click()

    def cheezyaddition(self):
        return self.element_to_be_clickable(By.XPATH, self.ADD_CHEEZYTIKKA)

    def add_products_cheezyaddition(self):
        time.sleep(4)
        self.cheezyaddition().click()

    def variation(self):
        return self.element_to_be_clickable(By.XPATH, self.VARIATION_CHEEZYTIKKA)

    def select_variation(self):
        time.sleep(2)
        self.variation().click()

    def flavour(self):
        return self.element_to_be_clickable(By.XPATH, self.FLAVOUR_CHEEZYTIKKA)

    def select_flavour(self):
        time.sleep(2)
        self.flavour().click()

    def quantity(self):
        return self.element_to_be_clickable(By.XPATH, self.ADD_QUANTITY_TIKKA)

    def add_quantity(self):
        self.quantity().click()

    def add_cheezy_tikka(self):
        return self.element_to_be_clickable(By.XPATH, self.ADD_TO_CART_PRODUCT)

    def click_add_cheezy_tikka(self):
        self.add_cheezy_tikka().click()

    def somewhat_local(self):
        time.sleep(10)
        return self.driver.find_element(By.CSS_SELECTOR, self.CLICK_SOMEWHAT_LOCAL)

    def click_somewhat_local(self):
        time.sleep(10)
        self.somewhat_local().click()

    def chicken_tikka(self):
        return self.element_to_be_clickable(By.XPATH, self.CLICK_CHICKEN_TIKKA)

    def click_chicken_tikka(self):
        self.chicken_tikka().click()

    def variation_chicken_tikka(self):
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.VARIATION_TIKKA)

    def click_variation_chicken_tikka(self):
        time.sleep(2)
        self.variation_chicken_tikka().click()

    def flavour_chicken_tikka(self):
        return self.element_to_be_clickable(By.XPATH, self.FLAVOUR_TIKKA)

    def click_flavour_chicken_tikka(self):
        time.sleep(2)
        self.flavour_chicken_tikka().click()

    def add_chicken_tikka(self):
        return self.element_to_be_clickable(By.XPATH, self.ADD_TO_CART_PRODUCT)

    def click_add_chicken_tikka(self):
        self.add_chicken_tikka().click()

    def starters(self):
        return self.element_to_be_clickable(By.XPATH, self.CLICK_STARTERS)

    def click_starters(self):
        time.sleep(2)
        self.starters().click()

    def cheesesticks(self):
        return self.element_to_be_clickable(By.CSS_SELECTOR, self.ADD_CHEESESTICKS)

    def add_cheesesticks(self):
        time.sleep(2)
        self.cheesesticks().click()

    def cart(self):
        return self.element_to_be_clickable(By.XPATH, self.CLICK_CART)

    def click_cart(self):
        time.sleep(2)
        self.cart().click()

    def checkout(self):
        return self.element_to_be_clickable(By.XPATH, self.CLICK_CHECKOUT)

    def click_checkout(self):
        time.sleep(2)
        self.checkout().click()


    def order_as_guest(self):
        return self.element_to_be_clickable(By.XPATH, self.ORDER_AS_GUEST)

    def click_order_as_guest(self):
        time.sleep(2)
        self.order_as_guest().click()


   # def select_location(self, location_name):
    #     location_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, ":r4:")))
    #     location_dropdown.click()
    #     time.sleep(2)
    #
    #     # Now, use the Select class to handle the dropdown
    #     location_select = Select(location_dropdown)
    #     # location_select.select_by_index(1)
    #     # location_select.select_by_visible_text(location_name)
    #     location_select.select_by_value(location_name)
    #     time.sleep(2)
    # def select_location2(self, location_name2):
    #     location_dropdown2 = self.wait.until(EC.element_to_be_clickable((By.XPATH,  "// body / div[3] / div[3] / div[2] / div[1] / div[1] / div[1] / div[3] / div[3] / div[1] / div[1] / div[1] / button[1] / * [1]")))
    #     location_dropdown2.click()
    #     time.sleep(2)
    #
    #     # Now, use the Select class to handle the dropdown
    #     location_select2 = Select(location_dropdown2)
    #     location_select2.select_by_visible_text(location_name2)
    #     time.sleep(2)
