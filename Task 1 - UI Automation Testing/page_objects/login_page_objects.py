from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_elements import LOGINELEMENTS

class LOGINPAGEOBJECTS:
    #initialize the driver
    def __init__(self,driver):
        self.driver = driver

        # locate username on the login page and save it in the user_name variable
        try:
            self.user_name = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.ID, LOGINELEMENTS.username_id )))
        except:
            pass

        # locate password on the login page and save it in the pass_word variable
        try:
            self.pass_word = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.ID, LOGINELEMENTS.password_id )))
        except:
            pass
    
        # locate login button on the login page and save it in the login_button variable
        try:
            self.login_button = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, LOGINELEMENTS.login_button_xpath )))
        except:
            pass

        # capture alert on the login page and save it in the screen_alert variable
        try:
            self.screen_alert = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.ID, LOGINELEMENTS.username_id )))
        except:
            self.screen_alert = None
        
    # function to return username element from login page
    def get_username(self):
        return self.user_name
    
    # function to return password element from login page
    def get_password(self):
        return self.pass_word
    
    # function to return login button element from login page
    def get_login_button(self):
        return self.login_button
    
    # function to return alert element from login page
    def get_alert(self):
        return self.screen_alert

  



