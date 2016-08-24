import os

import requests


AUTH_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')


def get_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
    payload = {
        'grant_type': "client_credentials",
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': "https://graph.microsoft.com/.default",
    }
    response = requests.post(AUTH_URL, data=payload)
    response.raise_for_status()
    token = response.json()['access_token']

    return token


if __name__ == '__main__':
    print(get_token(CLIENT_ID, CLIENT_SECRET))
