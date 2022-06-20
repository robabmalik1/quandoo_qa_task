from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
import pytest
import time
from locators.login_elements import LOGINELEMENTS
from automation.login_automation import LOGINAUTOMATION

logging.getLogger('WDM').setLevel(logging.NOTSET)


class TestTASK():
    @pytest.fixture
    def test_setUp(self):
        print('Test Case Started')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/login')
        time.sleep(2)
        self.login_automation = LOGINAUTOMATION(self.driver)
        self.correct_username = 'tomsmith'
        self.correct_password = 'SuperSecretPassword!'
        self.incorrect_username = 'Robab'
        self.incorrect_password = 'RobabTesting'

        yield
        self.driver.close()
        self.driver.quit()
        print('Test Case Completed')

    # testcase for login with empty username and empty password
    def test_01_login_with_empty_username_and_empty_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username='', password='')
        except:
            pass
        assert result != None, 'User logged in with empty username and password field, test case failed'

    # testcase for login with empty username and correct password
    def test_02_login_with_empty_username_and_correct_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username='', password=self.correct_password)
        except:
            pass
        assert result != None, 'User logged in with empty username field but correct password, test case failed'

    # testcase for login with correct username and empty password
    def test_03_login_with_correct_username_and_empty_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.correct_username, password='')
        except:
            pass
        assert result != None, 'User logged in with empty password field but correct username, test case failed'

    # testcase for login with empty username and incorrect password
    def test_04_login_with_empty_username_and_incorrect_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username='', password=self.incorrect_password)
        except:
            pass
        assert result != None, 'User logged in with empty usernmame field and incorrect password, test case failed'

    # testcase for login with incorrect username and empty password
    def test_05_login_with_incorrect_username_and_empty_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.incorrect_username, password='')
        except:
            pass
        assert result != None, 'User logged in with empty password field and incorrect username, test case failed'

    # testcase for login with incrrect username but correct password
    def test_06_login_with_incorrect_username_but_correct_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.incorrect_username, password=self.correct_password)
        except:
            pass
        assert result != None, 'ser logged in with incorrect username but correct password, test case failed'

    # testcase for login with correct username but incorrect password
    def test_07_login_with_correct_username_but_incorrect_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.correct_username, password=self.incorrect_password)
            time.sleep(2)
        except:
            pass
        assert result != None, 'User logged in with correct username but incorrect password, test case failed'

    # testcase for login with incorrect username and incorrect password
    def test_08_login_with_incorrect_username_and_incorrect_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.incorrect_username, password=self.incorrect_password)
            time.sleep(2)
        except:
            pass
        assert result != None, 'user logged in with incorrect username and incorrect password, test case failed'

    # testcase for login with correct username and correct password
    def test_09_login_with_correct_username_and_correct_password(self, test_setUp):
        try:
            result = self.login_automation.loginapplication(username=self.correct_username, password=self.correct_password)
            time.sleep(2)
        except:
            pass
        try:
            logout_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, LOGINELEMENTS.logout_button_xpath)))
        except:
            logout_btn = None
        assert logout_btn != None, 'User login failed with correct username and correct password, hence test case failed'
