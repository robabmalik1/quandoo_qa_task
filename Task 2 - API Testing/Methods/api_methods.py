import requests

class Methods:       
    def get_single_user_api(self,id):
        user_id = id
        # in order to get single user, id should not be empty or null
        if user_id == '':
            return None
        else:
            api_response = requests.get('https://reqres.in/api/users/' + str(user_id))
        
        return api_response
    
    def get_api_status_code(self,id):
        get_response = Methods.get_single_user_api(self,id)
        response_status_code = get_response.status_code
        
        return response_status_code
    
    def get_single_user_email(self,id):
        if id == '':
            email = ''
            return email
        else:
            get_response = Methods.get_single_user_api(self,id)
        
        if get_response.json() == {}:
            email = ''
            return email

        api_response_json = get_response.json()
        email = api_response_json['data']['email']
        
        return email
    
    def post_register_single_user(self,user_email,password):
        api_payload = {
            "email": user_email,
            "password":password
        }
        api_response = requests.post('https://reqres.in/api/register', data=api_payload)
        
        return api_response

    def get_registeration_status_code(self,user_email,password):
        api_response = Methods.post_register_single_user(self,user_email,password)
        api_status_code = api_response.status_code

        return api_status_code
    
    def get_registered_user_token(self,user_email,password):
        if user_email == '' or password == '':
            registeration_token = ''
            
            return registeration_token
        else:
            api_response = Methods.post_register_single_user(self,user_email,password)
            api_response_json = api_response.json()

            try:
                registeration_token = api_response_json['token']
            except:
                registeration_token = ''

        return registeration_token
    
    def post_login_user_api(self,user_email,password):
        api_payload = {
            "email": user_email,
            "password": password
        }
        api_response = requests.post('https://reqres.in/api/login', data=api_payload)

        return api_response
            
    def get_login_user_status_code(self,user_email,password):
        api_response = Methods.post_login_user_api(self,user_email,password)
        api_status_code = api_response.status_code
        
        return api_status_code
    
    def get_logined_user_token(self,user_email,password):
        if user_email == '' or password == '':
            login_token = ''
        else:
            api_response = Methods.post_login_user_api(self,user_email,password)
            api_response_json = api_response.json()

        try:
            login_token = api_response_json['token']
        except:
            login_token = ''
        
        return login_token

    def verify_valid_user_logged_in(self,user_email,password):
        registeration_token = Methods.get_registered_user_token(self,user_email,password)
        login_token = Methods.get_logined_user_token(self,user_email,password)
        
        if registeration_token == login_token and registeration_token and login_token:
            valid_user_status = True
        else:
            valid_user_status = False
        
        return valid_user_status
