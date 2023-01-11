import time

from selenium.webdriver.common.by import By

from selenium_test.practice_test.pages.basePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[1]")
    #                      (//input[@class='oxd-input oxd-input--active'])[1]
    PASSWORD = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    # LOGIN_BUTTON = (
    # By.XPATH, "((//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def do_login(self,username,password):
        time.sleep(2)
        self.do_send_keys(self.USERNAME,username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD,password)
        # self.do_click(self.LOGIN_BUTTON)



