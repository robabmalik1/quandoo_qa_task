from Methods.api_methods import Methods
import pytest


class TestApi():

    @pytest.fixture
    def test_setUp(self):
        self.valid_user_id = 2
        self.invalid_user_id = 23
        self.valid_password = 'Testing123'
        self.invalid_user_email = 'quandootest@quandoo.com'
        self.invalid_user_password = 'testing123'
        print('Starting test case')
        yield
        print('Ending test case')

    # # test case for get single user id api with user id = 2, is valid user id so api response should be status code = 200
    def test_01_verify_get_response_with_valid_user_id(self, test_setUp):
        api_status_code = Methods.get_single_user_api(self, id = self.valid_user_id)
        print('Test Case - Verify get single user api with valid user id, user id = 2, response code should be 200, else test case fails' )
        print('Get Status Code Returned'  + " "  + str(api_status_code.status_code))
        assert api_status_code.status_code == 200, 'API call failed with Valid paramters i.e valid user id'

    # test case for get single user id api with user id = 23 tat doesnt exist, api response should be status code = 404 and return empty array
    def test_02_verify_get_response_with_invalid_user_id(self, test_setUp):
        api_status_code = Methods.get_single_user_api(self, id = self.invalid_user_id)
        print('Test Case - Verify get single user api with invalid user id, user id = 23, response code should be 404, else test case fails' )
        print('Get Status Code Returned' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 404, 'API Called proceeded with invalid parameters i.e invalid user id'

    # test case for get single user id api with user id containing special characters
    def test_03_verify_get_response_with_sinlge_user_id_containig_special_characters(self, test_setUp):
        api_status_code = Methods.get_single_user_api(self, id = '*$')
        print('Test Case - Verify get single user api with user id containing special characters, user id = *$, response code should be 404 else test case fails' )
        print('Get Status Code Returned' + " " +  str(api_status_code.status_code))
        assert api_status_code.status_code == 404, 'API Called proceeded with invalid parameters'

    # test case for get single user id api with user id containing alphabets
    def test_04_verify_get_response_with_sinlge_user_id_containig_alphabets(self, test_setUp):
        api_status_code = Methods.get_single_user_api(self, id = 'a')
        print('Test Case - Verify get single user api with user id containing alphabet characters, user id = a, response code should be 404 else test case fails' )
        print('Get Status Code Returned' + " " +  str(api_status_code.status_code))
        assert api_status_code.status_code == 404, 'API Called proceeded with invalid parameters'

    # test case to test user api if there is no user id given
    def test_05_verify_get_response_with_no_user_id(self, test_setUp):
        api_status_code = Methods.get_single_user_api(self, id = '')
        print('Test Case - Verify get single user api with user id with empty user id, with empty user id') 
        print('With no user id  GET Api returns all users' )
        print('Get Status Code Returned' + " " +  str(api_status_code.status_code))
        assert api_status_code.status_code == 200, 'API Call didnt proceed with empty single user id'

    # user registeration test cases
    # to register single user, get email from get single user api, use that email for register-post api, status code returned should be 200
    # test case to register user with valid email and valid password
    def test_06_register_user_with_valid_credentials(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.valid_user_id)
        api_status_code = Methods.post_register_single_user(self, single_user_email, password = self.valid_password)
        print('Test Case - Register user with valid credentials, i.e with valid user email, response code should be 200 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 200, 'User registeration failed with vali credentials'

    # test case to register user that doesnt exist
    # should return status code == 400, else test case fails
    def test_07_register_user_with_invalid_user(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.invalid_user_id)
        api_status_code = Methods.post_register_single_user(self, single_user_email, password = self.valid_password)
        print('Test Case - Register user with invalid credentials, i.e with invalid user email,response code should be 400 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 400, 'User registered with invalid credentials, test case failed'

    # test case to register single user, with only valid user email and no password
    # api should return status code = 400, else test case fails
    def test_08_register_user_with_valid_email_but_no_password(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.valid_user_id)
        api_status_code = Methods.post_register_single_user(self, user_email = single_user_email, password = '')
        print('Test Case - Register user with only email no password, response code should be 400 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 400, 'User registered with only valid user email but no password, test case failed'

    # test case to register single user, with no user email and valid password
    # api should return status code = 400, else test case fails
    def test_09_register_user_with_no_email_but_valid_password(self, test_setUp):
        api_status_code = Methods.post_register_single_user(self, user_email = '', password = self.valid_password)
        print('Test Case - Register user with no email and only password, response code should be 400 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 400, 'User registered with no email only password, test case failed'

    # test case to register single user, with invalid user email and no password
    # api should return status code = 400, else test case fails
    def test_10_register_user_with_invalid_email_but_no_password(self, test_setUp):
        api_status_code = Methods.post_register_single_user(self, user_email = self.invalid_user_email, password = '')
        print('Test Case - Register user with invalid user email no password, response code should be 400 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 400, 'User registered with only user email but no password, test case failed'

    # test case to register single user, by sending no user email and no password
    #  api should return status code = 400
    def test_11_register_user_with_no_email_and_no_password(self, test_setUp):
        api_status_code = Methods.post_register_single_user(self, user_email = '', password = '')
        print('Test Case - Register user with no email and no password, response code should be 400 else test case fails')
        print('Post-Register API reponse code' + " " + str(api_status_code.status_code))
        assert api_status_code.status_code == 400, 'User registered with no user email and no password, test case failed'

    # test case for login valid user, with valid user id and valid email and valid password
    def test_12_login_user_with_valid_credentials(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.valid_user_id)
        register_api_response = Methods.post_register_single_user(self, single_user_email, password = self.valid_password)
        login_api_response = Methods.post_login_user_api(self, single_user_email, password = 'abc')
        print('Test Case - Login user with valid credentials, i.e with valid user email and password, response code should be 200 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 200, 'User not logged in'
        print('Registeration token and Login token should match, else test case fails')
        assert register_api_response.json()['token'] == login_api_response.json()['token'], 'Invalid user logged in, registeration token and login token do not match'

    # test case for login user,that doesnt exist,invalid user id
    def test_13_login_with_invalid_credentials(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.invalid_user_id)
        login_api_response = Methods.post_login_user_api(self, single_user_email, password = self.valid_password)
        print('Test Case - Login user with invalid credentials, i.e with invalid user email, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with user credentials that doesnt exist, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, single_user_email, password = self.valid_password)
        print('As user credentials aree invalid, Registeration token and Login token should match,, valid status should be False, else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'Invalid user logged in, registeration token and login token do not match'

    # test case for login user with valid user id and valid email but empty password field
    def test_14_login_with_valid_email_but_empty_password(self, test_setUp):
        single_user_email = Methods.get_single_user_email(self, self.valid_user_id)
        login_api_response = Methods.post_login_user_api(self, user_email = single_user_email, password = '')
        print('Test Case - Login user with valid email,but empty password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with empty user email, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = '', password = self.valid_password)
        print('As credentials are incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'Invalid user logged in, registeration token and login token do not match'

    # test case for login user with empty email field but valid password
    def test_15_login_with_empty_user_email_but_valid_password(self, test_setUp):
        login_api_response = Methods.post_login_user_api(self, user_email = '', password = self.valid_password)
        print('Test Case - Login user with empty email,but valid password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with empty user email, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = '', password = self.valid_password)
        print('As credentials are incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'Invalid user logged in, registeration token and login token do not match'

    # test case for login user with invalid user email but empty password field
    def test_16_login_with_invalid_email_but_empty_password(self, test_setUp):
        login_api_response = Methods.post_login_user_api(self, user_email = self.invalid_user_email, password = '')
        print('Test Case - Login user with invalid email,but empty password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with empty user email, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = self.invalid_user_email, password = '')
        print('As credentials are invalid and incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'Invalid user logged in, registeration token and login token do not match'

    # test case for login user with empty email field but invalid password
    def test_17_login_with_empty_user_email_but_invalid_password(self, test_setUp):
        login_api_response = Methods.post_login_user_api(self, user_email = '', password = self.invalid_user_password)
        print('Test Case - Login user with empty email,but invalid password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with empty user email, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = '', password = self.invalid_user_password)
        print('As credentials are invalid and incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'Invalid user logged in, registeration token and login token do not match'

    # test case to login user with invalid user email and invalid user password
    def test_18_login_with_invalid_user(self, test_setUp):
        login_api_response = Methods.post_login_user_api(self, user_email = self.invalid_user_email, password = self.invalid_user_password)
        print('Test Case - Login user with invalid email and invalid password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with invalid user email and invalid user password, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = self.invalid_user_email, password = self.invalid_user_password)
        print('As credentials are invalid and incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'User logged in with invalid token, test case failed'

    # test case to login user with empty user email and empty user password
    def test_19_login_with_empty_email_empty_password(self, test_setUp):
        login_api_response = Methods.post_login_user_api(self, user_email = '', password = '')
        print('Test Case - Login user with empty email and empty password, response code should be 400 else test case fails')
        print('Post-Login API reponse code' + " " + str(login_api_response.status_code))
        assert login_api_response.status_code == 400, 'User logged in with invalid user email and invalid user password, test case failed'
        valid_user_status = Methods.verify_valid_user_logged_in(self, user_email = '', password = '')
        print('As credentials are invalid and incomplete, Registeration token and Login token should match, valid status should be False else test case fails')
        print(valid_user_status)
        assert valid_user_status == False, 'User logged in with invalid token, test case failed'
