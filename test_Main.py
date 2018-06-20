import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages import MainPage
from Pages import FramePage


class NovTest(unittest.TestCase):
    driver = 0

    def setUp(self):
        selenium = webdriver.Chrome("./chromedriver")
        selenium.maximize_window()
        self.driver = selenium

    def tearDown(self):
        self.driver.close()

    def test_is_hero_slider_on_the_home_page(self):
        basePage = MainPage.MainPage(self.driver)
        basePage.navigate()
        assert basePage.is_hero_slider_exists()

    def test_is_hero_slider_exists_on_cute_page(self):
        basePage = MainPage.MainPage(self.driver)
        basePage.navigate()
        basePage.click_button((By.CLASS_NAME, "menu-cute"))
        assert (basePage.is_hero_slider_exists() is False)

#    def test_hover_over_cute(self):
#        websiteFrame = FramePage.FramePage(self.driver)
#        websiteFrame.hover_over_top_menu_cute()

if __name__ == '__main__':
    unittest.main()
