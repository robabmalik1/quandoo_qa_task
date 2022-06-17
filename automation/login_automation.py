from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from page_objects.login_page_objects import LOGINPAGEOBJECTS
import logging


class LOGINAUTOMATION:
    #initialize the driver
    def __init__(self,driver):
        self.driver = driver
        self.loginobjects = LOGINPAGEOBJECTS(self.driver)
    
    #function to input username in username field of login page
    def enter_username(self,username):
        try:
            user_name = self.loginobjects.get_username()
        except:
            pass
        logging.info('username' + ' - ' + username)
        print('username' + ' - ' + username)
        user_name.send_keys(username)
    
    #function to input password in password field of login page
    def enter_password(self,password):
        try:
            pass_word = self.loginobjects.get_password()
        except:
            pass
        logging.info('password'+ ' - ' + password )
        print('password' + ' - ' + password)
        pass_word.send_keys(password)
    
    #click login button present on login page 
    def click_login_button(self):
        try:
            login_button = self.loginobjects.get_login_button()
        except:
            pass
        login_button.click()
    
    #capture any alerts present on page
    def capture_alert(self):
        try:
            screen_alert = self.loginobjects.get_alert()
        except:
            screen_alert = None
                
    def loginapplication(self,username,password):
        print('Login Form - Steps to execute test case')
        print('Step - 1: Input username')
        self.enter_username(username)
        time.sleep(2)

        print('Step - 2: Input password')
        self.enter_password(password)
        time.sleep(2)

        print('Step - 3: Click login button')
        self.click_login_button()
        
        





