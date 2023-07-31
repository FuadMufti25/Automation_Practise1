import pytest
from pages.faq import FAQPage


@pytest.mark.usefixtures("setup")
class Test_FAQ():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.faq = FAQPage(self.driver)

    def test_tc02(self):
        self.faq.select_location("Lahore")
        self.faq.select_location2("Johar Town Phase 1 Block G1")
        self.faq.click_selectbutton()
        self.faq.scroll_down_to_end()
        self.faq.close_modal()
        self.faq.click_faq1()
        self.faq.click_faq2()
        self.faq.click_faq3()
        self.faq.click_faq4()
        self.faq.click_faq5()



