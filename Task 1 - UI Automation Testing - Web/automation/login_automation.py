from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import time
from page_objects.login_page_objects import LOGINPAGEOBJECTS
from locators.login_elements import LOGINELEMENTS


class LOGINAUTOMATION:
    # initialize the driver
    def __init__(self, driver):
        self.driver = driver
        self.loginobjects = LOGINPAGEOBJECTS(self.driver)

    # function to input username in username field of login page
    def enter_username(self, username):

        try:
            user_name = self.loginobjects.get_username()
        except:
            pass

        logging.info('username' + ' - ' + username)
        print('username' + ' - ' + username)

        user_name.send_keys(username)

    # function to input password in password field of login page
    def enter_password(self, password):

        try:
            pass_word = self.loginobjects.get_password()
        except:
            pass

        logging.info('password' + ' - ' + password)
        print('password' + ' - ' + password)

        pass_word.send_keys(password)

    # click login button present on login page
    def click_login_button(self):

        try:
            login_button = self.loginobjects.get_login_button()
        except:
            pass

        login_button.click()

    # capture any alerts present on page
    def capture_alert(self):

        try:
            screen_alert = self.loginobjects.get_alert()
        except:
            screen_alert = None

    # capture alert message
    def get_alert_message(self):

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, LOGINELEMENTS.alert_id))).text
        except:
            alert_text = 'No Alert'

        return alert_text

    def loginapplication(self, username, password):

        print('Login Form - Steps to execute test case')
        print('Step - 1: Input username')

        self.enter_username(username)
        time.sleep(2)

        print('Step - 2: Input password')

        self.enter_password(password)
        time.sleep(2)

        print('Step - 3: Click login button')
        self.click_login_button()

        # get alert message on screen
        alert_text = self.get_alert_message()

        # print alert message
        print('Alert Message on Screen' + ' ' + alert_text)

        # for unsuccessful login, we have used username field element for verification as sometimes, alert may not display
        # so for unsuccuessful login it checks whether user is on the login screen or not
        try:
            username_field = self.loginobjects.get_username()
        except:
            username_field = None

        return username_field
