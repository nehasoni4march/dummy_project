import time

import pytest
from selenium import webdriver

from selenium_test.practice_test.pages.loginPage import LoginPage


@pytest.fixture(scope="class")
def init_driver(request):
    print("__________setup_____________")
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    # request.cls.loginpage=LoginPage(driver)


    print("_________teardown__________")
    yield

    # driver.close()
