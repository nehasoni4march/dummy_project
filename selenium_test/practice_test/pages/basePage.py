import traceback

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        try:
            ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            ele.clear()
            ele.send_keys(text)
            print("sending text=", text)
        except Exception as error:
            print(traceback.format_exc())

    def is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        return element

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return element
