# -*- coding: utf-8 -*-
# Code modified from Google, licensed under the Apache License, Version 2.0
from bot import Bot
from datastore import model_datastore
from flask import current_app, Flask, request
from request_handler import RequestHandler

bot = Bot()
request_handler = RequestHandler(bot)

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	with app.app_context():
		model = get_model()
		model.init_app(app)

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

	return app

def get_model():
	model_backend = current_app.config['DATA_BACKEND']
	if model_backend == 'datastore':
		model = model_datastore
	else:
		raise ValueError(
			"No appropriate databackend configured. "
			"Please specify datastore.")
	return model
