from . import auth


def _make_auth_headers():
    token = auth.get_token()
    return {'Authorization': 'Bearer {0}'.format(token)}
