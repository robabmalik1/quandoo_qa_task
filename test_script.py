import logging
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from locators.login_elements import LOGINELEMENTS
from page_objects.login_page_objects import LOGINPAGEOBJECTS
from automation.login_automation import LOGINAUTOMATION
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTASK():
    @pytest.fixture
    def test_setUp(self):
        logging.info('Start')
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/login')
        time.sleep(2)
        self.login_automation = LOGINAUTOMATION(self.driver)
        yield
        self.driver.close()
        self.driver.quit()
        print('test case completed')

    # @pytest.mark.parametrize("username,password,message",[

    # (" ", " ","username is invalid"),
    # (" ", "SuperSecretPassword!","username is invalid")

    # # ("robab","123", "username is invalid"), 
    # # ("tomsmith", "123", "password is invalid"), 
    # # ("123", "SuperSecretPassword!","username is invalid")
    # ]
    # )
    # def test_01(self,test_setUp,username,password,message):
    #     try:
    #         logging.info('login function')
    #         # login_automation = LOGINAUTOMATION(self.driver)
    #         self.login_automation.loginapplication(username,password)
    #     except:
    #         pass

    #     try:
    #         alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
    #     except:
    #         alert_text =''
    #     assert message in alert_text


    def test_01_testcase_for_empty_username_and_empty_password(self,test_setUp,username='',password=''):
        try:
            self.login_automation.loginapplication(username,password)
        except:
            pass
        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = None
        print(alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        
        assert username_field!=None,'Logged in with empty username and password field, test case failed'
    
    def test_02_testcase_for_empty_username_and_correct_password(self,test_setUp,username='',password='SuperSecretPassword!'):
        try:
            self.login_automation.loginapplication(username,password)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = None
        print(alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        
        assert username_field!=None,'Logged in with empty username field but correct password, test case failed'
    
    def test_03_testcase_for_correct_username_and_empty_password(self,test_setUp,username='tomsmith',password=''):
        try:
            self.login_automation.loginapplication(username,password)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        
        except:
            alert_text = 'no alert'
        print('Alert Message on Screen'+ ' ' + alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        assert username_field!=None,'Logged in with empty password field but correct username, test case failed'
    
    def test_04_testcase_for_incorrect_username_but_correct_password(self,test_setUp,username='robab',password='SuperSecretPassword!'):
        try:
            self.login_automation.loginapplication(username,password)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = 'no alert present'
        print('Alert Message on Screen'+ ' - ' + alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        assert username_field!=None,'Logged in with incorrect username but correct password, test case failed'
        
    def test_05_testcase_for_correct_username_but_incorrect_password(self,test_setUp,username='tomsmith',password='randompassword'):
        try:
            self.login_automation.loginapplication(username,password)
            time.sleep(2)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = 'no alert present'
        print('Alert Message on Screen'+ ' - ' + alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        assert username_field!=None,'Logged in with correct username but incorrect password, test case failed'

    def test_06_testcase_for_incorrect_username_and_incorrect_password(self,test_setUp,username='robab',password='robabqatest'):
        try:
            self.login_automation.loginapplication(username,password)
            time.sleep(2)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = 'no alert present'
        print('Alert Message on Screen'+ ' - ' + alert_text)

        try:
            username_field = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.username_id)))
        except:
            username_field = None
        assert username_field!=None,'Logged in with incorrect username and incorrect password, test case failed'

    def test_07_testcase_for_correct_username_but_incorrect_password(self,test_setUp,username='tomsmith',password='SuperSecretPassword!'):
        try:
            self.login_automation.loginapplication(username,password)
            time.sleep(2)
        except:
            pass

        try:
            alert_text = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.alert_id))).text
        except:
            alert_text = 'no alert present'
        print('Alert Message on Screen'+ ' - ' + alert_text)

        try:
            logout_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,LOGINELEMENTS.logout_button_xpath)))
        except:
            logout_btn = None
        assert logout_btn!=None,'Login failed with correct username and correct password, hence test case failed'

    
