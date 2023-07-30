import pytest
from pages.homepage import LaunchPage




@pytest.mark.usefixtures("setup")
class Test_Homepage():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    def test_tc01(self):
        self.lp.click_selectbutton()
        self.lp.add_products_cheezyaddition()
        self.lp.select_variation()
        self.lp.select_flavour()
        self.lp.add_quantity()
        self.lp.click_add_cheezy_tikka()
        self.lp.click_somewhat_local()
        self.lp.click_chicken_tikka()
        self.lp.click_variation_chicken_tikka()
        self.lp.click_flavour_chicken_tikka()
        self.lp.click_add_chicken_tikka()
        self.lp.click_starters()
        self.lp.add_cheesesticks()
        self.lp.scroll_down(1500)
        self.lp.click_cart()
        self.lp.click_checkout()
        # lp.select_location("Lahore")
        # lp.select_location2("Johar Town Phase 1 Block G1")



