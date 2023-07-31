import pytest
from pages.homepage import LaunchPage
from pages.order import OrderPage


@pytest.mark.usefixtures("setup")
class Test_Homepage():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.op = OrderPage(self.driver)

    def test_tc03(self):
        self.lp.select_location("Lahore")
        self.lp.select_location2("Johar Town Phase 1 Block G1")
        self.lp.click_selectbutton()
        self.lp.add_products_cheezyaddition()
        self.lp.select_variation()
        self.lp.select_flavour()
        self.lp.add_quantity()
        self.lp.click_add_cheezy_tikka()
        # self.lp.click_somewhat_local()
        self.lp.click_chicken_tikka()
        self.lp.click_variation_chicken_tikka()
        self.lp.click_flavour_chicken_tikka()
        self.lp.click_add_chicken_tikka()
        self.lp.click_starters()
        self.lp.add_cheesesticks()
        self.lp.scroll_down(1500)
        self.lp.click_cart()
        self.lp.click_checkout()
        self.lp.click_order_as_guest()
        self.op.enter_name("Fuad Mufti")
        self.op.enter_mobile("3321403309")
        self.op.click_address()
        self.op.enter_address_field("PIA SOCIETY LAHORE")
        self.op.click_save_address()
        self.op.enter_special_instructions("No instructions at all")


