from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):

    waitConfig = 20

    def __init__(self, driver):
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()

    def locate_element(self, location):
        return WebDriverWait(self.driver, self.waitConfig).until(
            EC.presence_of_element_located(location)
        )

    def get_text(self, location):
        elem = self.locate_element(location)
        return elem.text

    def fill_form(self, location, value):
        elem = self.locate_element(location)
        elem.send_keys(value)

    def click_button(self, location):
        elem = self.locate_element(location)
        elem.click()

    def hover_over(self, location):
        elem = self.locate_element(location)
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()