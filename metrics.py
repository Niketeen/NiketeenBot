# -*- coding: utf-8 -*-

import config
import requests
import json

URL_TEMPLATE = 'https://api.botan.io/track?token={token}&uid={uid}&name={name}'

def make_json(message):
    data = {}
    data['message_id'] = message.message_id
    data['from'] = {}
    data['from']['id'] = message.from_user.id
    if message.from_user.username is not None:
        data['from']['username'] = message.from_user.username
    data['chat'] = {}
    data['chat']['id'] = message.chat.id
    return data

def track(msg, name='Message'):
    global url_template
    url = URL_TEMPLATE.format(token=str(config.YandexMetricsAPIKey), uid=str(msg.chat.id), name=name)
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.post(url, data=json.dumps(make_json(msg)), headers=headers)
        return r.json()
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.RequestException as e:
        print(e)
    return False
