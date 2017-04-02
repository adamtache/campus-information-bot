# -*- coding: utf-8 -*-
import facebook_replier

from flask import Flask, request
 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_webhook():
	"""Handles verification of Facebook messenger bot
	"""
	return request.args.get('hub.challenge', '')

@app.route('/', methods=['POST'])
def post_webhook():
    data = request.json
    messaging_data = _get_entry_messaging_data(data)
    sender = _get_sender(messaging_data)
    message = _get_message(messaging_data)
    facebook_replier.reply(sender, message)
    return "ok", 200

def _get_sender(messaging_data):
    return messaging_data['sender']['id']

def _get_message(messaging_data):
    return messaging_data['message']['text']

def _get_entry_messaging_data(data):
    return data['entry'][0]['messaging'][0]

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
 
if __name__ == '__main__':
    app.run(debug=True)
