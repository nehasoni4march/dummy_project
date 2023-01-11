import pytest

from selenium_test.practice_test.pages.loginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login_functionality(self):
        loginpage=LoginPage(self.driver)
        loginpage.do_login("Admin","admin123")
