import requests

from . import auth
from utils import _make_auth_headers


def send_message(serviceUrl, conversation_id, activity, activity_id=None):
    connect_url = '{0}/v3/conversations/{1}/activities/'.format(serviceUrl, conversation_id)

    if activity_id:
        connect_url += activity_id

    headers = _make_auth_headers()
    response = requests.post(
        url=connect_url,
        json=activity,
        headers=headers,
    )
    response.raise_for_status()

    return response
