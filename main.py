# source 1

# import library that allows us to pull data from websites
import requests

# requests data from url below
request = requests.get(
    'https://gsu.campuslabs.com/engage/events?perks=FreeFood')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content, features='html5lib')

link = 'https://gsu.campuslabs.com/engage/events?perks=FreeFood'

# filters soup to only display what is specified
specificData = soup.find_all('div')

# finds and prints alternative text for images at above url
for x in specificData:
    print(x)

import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log('Recieved {}'.format(data))

    # We don't want to reply to ourselves!
    if data['name'] != 'FoodBot':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)

    return "ok", 200


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('a8100d0d031f1cb4008bb9b169'),
        'text': msg,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def log(msg):
    print(str(msg))
    sys.stdout.flush()
