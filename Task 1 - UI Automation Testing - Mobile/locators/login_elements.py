class LOGINELEMENTS:

    # locators for elements necassary for login process
    username_xpath = '/html/body/div[2]/div/div/form/div[1]/div/input'
    password_xpath = '/html/body/div[2]/div/div/form/div[2]/div/input'
    login_button_xpath = '/html/body/div[2]/div/div/form/button'

    # locators for elements to verify login was successful
    logout_button_xpath = '//i[@class="icon-2x icon-signout"]'

    # locators for caputring alert messages / error messages
    alert_id = 'flash-messages'
    
    