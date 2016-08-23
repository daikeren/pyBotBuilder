def _make_auth_headers(token):
    return {'Authorization': 'Bearer {0}'.format(token)}
