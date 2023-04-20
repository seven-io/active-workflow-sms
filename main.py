import os

from flask import Flask
from flask import jsonify
from flask import request
from sms77api.Sms77api import Sms77api

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle():
    return handle_agent(SevenSmsAgent, request)


def handle_agent(cls, req):
    """Helper that routes 'method calls' to a real agent object."""

    content = req.json
    method = content['method']
    params = content.get('params')

    if method == 'register':
        response = cls.register()
    elif method == 'check':
        response = cls(params).check()
    elif method == 'receive':
        response = cls(params).receive(params['message'])
    else:
        response = {}

    return jsonify(response)


class SevenSmsAgent:
    def __init__(self, params):
        """Set some convenience variables.
        Object is created from scratch on each method invocation"""
        self.credentials = params['credentials']
        self.options = params['options']
        self.memory = params['memory'] or {}

    # noinspection PyMethodParameters
    def register():
        """Register our metadata"""

        return {
            'result': {
                'default_options': {
                    'apiKey': '{% credential seven_api_key %}',
                    'debug': False,
                    'delay': None,
                    'flash': False,
                    'foreign_id': None,
                    'from': None,
                    'label': None,
                    'no_reload': False,
                    'performance_tracking': False,
                    'text': None,
                    'to': None,
                    'ttl': None,
                    'udh': None,
                    'unicode': False,
                    'utf8': False,
                },
                'description': 'Agent to send SMS via seven.io.',
                'display_name': 'seven SMS Agent',
                'name': 'SevenSmsAgent',
            }
        }

    def check(self):
        """This is run on schedule. Do something useful."""
        messages = []

        if self.memory.get('last_message'):
            messages.append(self.memory['last_message'])

        memory = self.memory.copy()
        memory.pop('last_message', None)

        return {
            'result': {
                'errors': [],
                'logs': ['Check done'],
                'memory': memory,
                'messages': messages,
            }
        }

    def receive(self, message):
        """Process message and do something with it."""
        errors = []
        messages = []
        payload = message['payload']

        self.memory['last_message'] = payload

        payload.pop('details', None)
        payload.pop('return_msg_id', None)
        payload['json'] = 1

        api_key = payload.pop('apiKey', os.getenv('SEVEN_API_KEY'))
        if api_key is None:
            errors.append('Missing API key')

        text = payload.pop('text', None)
        if text is None:
            errors.append('Missing text')

        to = payload.pop('to', None)
        if to is None:
            errors.append('Missing to')

        if 0 == len(errors):
            res = Sms77api(api_key, 'active-workflow').sms(to, text, payload)
            messages.append(res)

        return {
            'result': {
                'errors': errors,
                'logs': ['New message received'],
                'memory': self.memory,
                'messages': messages,
            }
        }


if __name__ == '__main__':
    app.run()
