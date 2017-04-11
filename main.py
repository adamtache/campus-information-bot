# -*- coding: utf-8 -*-
from bot.bot import CampusBot
from bot.request_handler import RequestHandler
from wit.wit_handler import WitHandler
from flask import Flask, request
import requests
from requests_toolbelt.adapters import appengine

# Use AppEngineAdapter to support GAE with requests
appengine.monkeypatch()
app = Flask(__name__)
bot = CampusBot()
wit_handler = WitHandler()
request_handler = RequestHandler(bot, wit_handler)

@app.route('/', methods=['GET'])
def get_webhook():
	"""Handles verification of Facebook messenger bot
	"""
	return request.args.get('hub.challenge', '')

@app.route('/', methods=['POST'])
def post_webhook():
	return request_handler.handle(request)

@app.errorhandler(404)
def page_not_found(e):
	return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500
 
if __name__ == '__main__':
	app.run(debug=True)
