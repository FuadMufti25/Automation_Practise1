from selenium.webdriver.common.by import By
import time
from base.basedrivers import BaseDrivers


class FAQPage(BaseDrivers):
    def __init__(self, driver):
        self.driver = driver

    # locators
    SELECT_BUTTON = "//button[normalize-space()='Select']"
    FAQ1 = "//body/div[@id='__next']/div[@class='MuiBox-root blink-style-79elbk']/div[@class='root']/div[@class='MuiContainer-root blink-style-10ur324']/div/div[1]/div[1]/div[2]//*[name()='svg']"
    FAQ2 = "//div[@class='MuiContainer-root blink-style-10ur324']//div//div[2]//div[1]//div[2]//*[name()='svg']"
    FAQ3 = "//body/div[@id='__next']/div[@class='MuiBox-root blink-style-79elbk']/div[@class='root']/div[@class='MuiContainer-root blink-style-10ur324']/div/div[3]/div[1]/div[2]//*[name()='svg']"
    FAQ4 = "//body/div[@id='__next']/div[@class='MuiBox-root blink-style-79elbk']/div[@class='root']/div[@class='MuiContainer-root blink-style-10ur324']/div/div[4]/div[1]/div[2]//*[name()='svg']"
    FAQ5 = "//body/div[@id='__next']/div[@class='MuiBox-root blink-style-79elbk']/div[@class='root']/div[@class='MuiContainer-root blink-style-10ur324']/div/div[5]/div[1]/div[2]//*[name()='svg']"
    FAQ6 = "//body/div[@id='__next']/div[@class='MuiBox-root blink-style-79elbk']/div[@class='root']/div[@class='MuiContainer-root blink-style-10ur324']/div/div[6]/div[1]/div[2]//*[name()='svg']//*[name()='path' and contains(@d,'M16.59 8.5')]"
    CLOSE_MODAL = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium blink-style-vubbuv'])[55]"
    CLOSE_FAQ2 = "div[id='product-item-250732'] div button[aria-label='Add To Cart']"
    CLOSE_FAQ3 = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium blink-style-vubbuv'])[1]"
    CLOSE_FAQ4 = "//button[normalize-space()='Checkout']"
    CLOSE_FAQ5 = "//button[contains(text(),'Somewhat Local')]"

    # location by current location
    def get_location(self):
        return self.element_to_be_clickable(By.XPATH, self.SELECT_BUTTON)

    def click_selectbutton(self):
        self.get_location().click()

    def modal(self):
        return self.element_to_be_clickable(By.XPATH, self.CLOSE_MODAL)

    def close_modal(self):
        time.sleep(1)
        self.modal().click()
        time.sleep(5)

    def faq1(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ1)

    def click_faq1(self):
        # time.sleep(4)
        self.faq1().click()

    def faq2(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ2)

    def click_faq2(self):
        # time.sleep(4)
        self.faq2().click()

    def faq3(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ3)

    def click_faq3(self):
        # time.sleep(4)
        self.faq3().click()

    def faq4(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ4)

    def click_faq4(self):
        # time.sleep(4)
        self.faq4().click()

    def faq5(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ5)

    def  click_faq5(self):
        # time.sleep(4)
        self.faq5().click()

    def faq6(self):
        return self.element_to_be_clickable(By.XPATH, self.FAQ6)

    def click_faq6(self):
        # time.sleep(4)
        self.faq6().click()

    def close_faq1(self):
        time.sleep(2)
        self.faq1().click()

    def close_faq2(self):
        time.sleep(2)
        self.faq2().click()

    def close_faq3(self):
        time.sleep(2)
        self.faq3().click()

    def close_faq4(self):
        # time.sleep(4)
        self.faq4().click()
