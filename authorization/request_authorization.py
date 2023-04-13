import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import cache


HOST = "https://accounts.spotify.com"
CLIENT_ID = '49e76d4088584b90bb5f0f480f945ed7'
ENC_REDIRECT_URI = 'http%3A%2F%2Ftestaremanualamaxim.com%2Fcallback'
REDIRECT_URI = 'http://testaremanualamaxim.com/callback'
SCOPE = 'ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private'
USERNAME = (By.ID, 'login-username')
PASSWORD = (By.ID, 'login-password')
LOGIN_BUTTON = (By.ID, 'login-button')
CLIENT_SECRET = '67d5a4b7834b4a3e8f10ddc5581ff2ca'
GRANT_TYPE = 'authorization_code'




@cache
def get_authentication_code():
    code_url = f'{HOST}/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={ENC_REDIRECT_URI}&scope={SCOPE}'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(code_url)

    driver.find_element(*USERNAME).send_keys("woodrow_ledner@gmail.com")
    driver.find_element(*PASSWORD).send_keys("Testaremanuala*123")
    driver.find_element(*LOGIN_BUTTON).click()

    details = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'details-button')))
    url = driver.current_url
    _, auth_code = url.split('=', maxsplit=1)
    return auth_code
   

@cache
def make_auth_header():
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': get_authentication_code(),
        'grant_type': GRANT_TYPE
    }
    api_url = f'{HOST}/api/token'
    response = requests.post(api_url, data=data, headers=header)
    response_data = response.json()
    token = response_data['access_token']
    return dict(Authorization=f"Bearer {token}")


