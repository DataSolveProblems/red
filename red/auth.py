import requests
import requests.auth

ACCESS_TOKEN_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
USER_AGENT = 'Red1.1 by JJ'

def authorize(client_id, client_secret, username, password):
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    payload = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    response = requests.post(
        ACCESS_TOKEN_ENDPOINT,
        auth=client_auth,        
        headers={'User-Agent': USER_AGENT},
        data=payload
    )
    if 'access_token' in response.json():
        return {'access_token': response.json()['access_token']}
    else:        
        return response.json()