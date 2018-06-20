from Framework import Page
from selenium.webdriver.common.by import By
from selenium.common import exceptions


class MainPage(Page.BasePage):

    hero_slider_locator = (By.CLASS_NAME, "hero_slider")

    def navigate(self):
        self.driver.get("http://www.icepop.com")

    def is_hero_slider_exists(self):
        try:
            self.locate_element(self.hero_slider_locator)
            return True
        except exceptions.TimeoutException:
            return False



