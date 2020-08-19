import json
import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
METHOD_URL = os.getenv('METHOD_URL')
VERSION_API = os.getenv('VERSION_API')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def get_status(user_id):
    params = {
        'access_token': ACCESS_TOKEN,
        'user_ids': user_id,
        'fields': 'online',
        'v': VERSION_API
    }
    response = requests.post(
        f'{METHOD_URL}users.get', params=params).json()
    status = response['response'][0]['online']
    return status


def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
