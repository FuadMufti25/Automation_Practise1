from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

class DemoLocateElementById():
    def locate_element_by_id(self):
        # driver= webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver = webdriver.Chrome()
        driver.get("https://www.cheezious.com/")
        driver.maximize_window()
        time.sleep(10)
        driver.find_element(By.XPATH, "//div[@class='MuiBox-root blink-style-12pqxh8']").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Select'])[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "// body / div[3] / div[3] / div[2] / div[1] / div[2] / div[1] / div[2] / div[1] / div[1] / span[1] / input[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, " // body / div[3] / div[3] / div[2] / div[1] / div[2] / div[1] / div[4] / div[4] / div[1] / span[1] / input[1]").click()
        driver.find_element(By.XPATH, "   // body / div[3] / div[3] / div[2] / div[1] / div[3] / div[1] / div[1] / button[2] / * [1]").click()
        driver.find_element(By.XPATH, "  // body / div[3] / div[3] / div[2] / div[1] / div[3] / div[1] / button[1]").click()
        time.sleep(4)


    # def starters(self): 
        driver.find_element(By.XPATH, "//div[contains(text(),'Starters')]").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "div[id='product-item-250732'] div button[aria-label='Add To Cart']").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium blink-style-vubbuv'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "(//button[normalize-space()='Checkout'])[1]").click()
        time.sleep(4)



findbyid = DemoLocateElementById()
findbyid.locate_element_by_id()
# findbyid.starters()
