import requests

from utils import _make_auth_headers


def _make_state_url(channel_id, user_id, conversation_id):
    state_url = "https://state.botframework.com/v3/botstate/{0}".format(channel_id)

    if conversation_id:
        state_url += '/conversations/{0}'.format(conversation_id)

    if user_id:
        state_url += '/users/{0}'.format(user_id)

    return state_url


def get_state(channel_id, user_id=None, conversation_id=None):
    headers, state_url = _make_auth_headers(), _make_state_url(channel_id, user_id, conversation_id)

    response = requests.get(state_url, headers=headers)
    response.raise_for_status()

    return response.json()

def set_state(channel_id, state, user_id=None, conversation_id=None):
    headers, state_url = _make_auth_headers(), _make_state_url(channel_id, user_id, conversation_id)

    response = requests.post(state_url, headers=headers, json=state)
    response.raise_for_status()

    return response.json()
