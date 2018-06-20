from Framework import Page
from selenium.webdriver.common.by import By
from selenium.common import exceptions


class FramePage(Page.BasePage):

    def click_top_menu_blue(self):
        self.click_button((By.CLASS_NAME, "menu-blue"))

    def hover_over_top_menu_cute(self):
        self.hover_over((By.CLASS_NAME, "menu-blue"))

    def click_top_menu_cute(self):
        self.click_button((By.CLASS_NAME, "menu-cute"))

