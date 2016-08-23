import os

import requests


AUTH_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"


def get_token(client_id, client_secret):
    payload = {
        'grant_type': "client_credentials",
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': "https://graph.microsoft.com/.default",
    }
    response = requests.post(AUTH_URL, data=payload)
    return response.json()


if __name__ == '__main__':
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    print(get_token(CLIENT_ID, CLIENT_SECRET))