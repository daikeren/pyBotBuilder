import json

from bottle import route, run, request

import botbuilder


@route('/webhook/', method='POST')
def index():
    payload = request.json
    print(payload)
    activity = {
        'from': payload['recipient'],
        'type': 'message',
        'text': payload['text']
    }
    response = botbuilder.connector.send_message(payload['serviceUrl'], payload['conversation']['id'], activity)
    return ""

run(host='localhost', port=8000)
