# -*- coding: utf-8 -*-
from bot.bot import CampusBot
from util.facebook import facebook_parser

from flask import Flask, request
 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_webhook():
	"""Handles verification of Facebook messenger bot
	"""
	return request.args.get('hub.challenge', '')

@app.route('/', methods=['POST'])
def post_webhook():
	sender, message = facebook_parser.parse(request.json)
	CampusBot().handle(sender, message)
	return "ok", 200

@app.errorhandler(404)
def page_not_found(e):
	return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500
 
if __name__ == '__main__':
	app.run(debug=True)
