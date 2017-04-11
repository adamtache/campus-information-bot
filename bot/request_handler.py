# -*- coding: utf-8 -*-
from util.facebook.facebook_parser import parse
from util.facebook.webhook_callbacks import InvalidWebhookCallback
from util.facebook.webhook_callbacks import WebhookCallback
from util.facebook.callback_data import DATA_TYPE_MESSAGE
from util.facebook.callback_data import DATA_TYPE_POSTBACK
from requestors.facebook_get_started_button import GET_STARTED_PAYLOAD

class RequestHandler(object):

	def __init__(self, bot, wit_handler):
		self.bot = bot
		self.wit_handler = wit_handler

	def handle(self, request):
		callback = parse(request.json)
		if type(callback) is InvalidWebhookCallback:
			return "ok", 200
		self._handle_callback(callback)
		# Must send back 200 to facebook within 20 seconds
		return "ok", 200

	def _handle_callback(self, callback):
		sender = callback.sender
		self._setup_fb_user_if_needed(sender)
		for data in callback.data:
			data_type = data.data_type
			if data_type is DATA_TYPE_MESSAGE:
				self._handle_message(data, sender)
			elif data_type is DATA_TYPE_POSTBACK:
				self._handle_postback(data, sender)

	def _setup_fb_user_if_needed(self, sender):
		if self.bot.user is None:
			self.bot.setup_facebook_user(sender)

	def _handle_message(self, message, sender):
		self.wit_handler.handle(session_id=sender, message=message)

	def _handle_postback(self, postback, sender):
		payload = postback.payload
		if payload == GET_STARTED_PAYLOAD:
			self._handle_get_started(sender)

	def _handle_get_started(self, sender):
		self.bot.reply_welcome(sender)
