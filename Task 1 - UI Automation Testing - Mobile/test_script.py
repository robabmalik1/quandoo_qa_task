from appium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

import logging
logging.getLogger('WDM').setLevel(logging.NOTSET)

from automation.login_automation import LOGINAUTOMATION


capabilities = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'S21 Ultra 5G',

    'automationName': 'UIAutomator2',
    'browserName': 'Chrome',
    'chromeOptions': {"w3c": "false"},
}


class TestTASK():
    @pytest.fixture
    def test_setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', capabilities)
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.login_automation = LOGINAUTOMATION(self.driver)
        self.correct_username = 'tomsmith'
        self.correct_password = 'SuperSecretPassword!'
        self.incorrect_username = 'Robab'
        self.incorrect_password = 'RobabTesting'

        yield
        self.driver.close()
        self.driver.quit()
        print('Test Case Completed')

    # paramterize the test cases instead of repeating the same test function for all paramterize.
    # send all test data as parameter, using pytest paramterize feature
    @pytest.mark.parametrize("username,password,message",
                             [("", "", "Test Case - 1 : Login with Empty Username and Password"),
                              ("", "SuperSecretPassword!","Test Case - 2 : Login with empty username but correct password"),
                              ("tomsmith", "", "Test Case - 3: Login with correct username but empty password"),
                              ("", "RobabTesting123","Test Case - 4 : Login with empty username but incorrect password"),
                              ("Robab", "", "Test Case - 5 : Login with incorrect username but empty password"),
                              ("Robab", "SuperSecretPassword!","Test Case - 6 : Login with incorrect username but correct password"),
                              ("tomsmith", "RobabTesting","Test Case - 7 : Login with correct username but inorrect password"),
                              ("Robab", "Robab Testing", "Test Case - 8 : Login with incorrect username and incorrect password")
                              ])
    def test_1_login(self, test_setUp, username, password, message):
        print(message)

        try:
            result = self.login_automation.loginapplication(username, password)
        except:
            pass

        assert result != None, 'User logged in with invalid credentials, test case failed'

    @pytest.mark.parametrize("username,password,message",[("tomsmith", "SuperSecretPassword!", "Test Case - 9 : Login with Correct Username and Correct Password")])
    def test_2_successful_login(self, test_setUp, username, password, message):
        print(message)

        try:
            result = self.login_automation.loginapplication(username, password)
        except:
            pass
        time.sleep(2)
        assert ' Logout' in self.driver.page_source, 'User log in failed with correct username and correct password field, test case failed'
