# -*- coding: utf-8 -*-
from payload_handler import PostbackHandler
from util.facebook.facebook_parser import parse
from util.facebook.webhook_callbacks import InvalidWebhookCallback
from util.facebook.webhook_callbacks import WebhookCallback
from util.facebook.callback_data import DATA_TYPE_MESSAGE
from util.facebook.callback_data import DATA_TYPE_POSTBACK
from util.constants.tokens import WIT_ACCESS_TOKEN
from wit.wit import Wit
from wit.actions.actions import get_actions

class RequestHandler(object):

	def __init__(self, bot):
		self.bot = bot
		self.wit_client = Wit(
			access_token=WIT_ACCESS_TOKEN,
			actions=get_actions(bot.replier),
		)
		self.postback_handler = PostbackHandler(self.bot)

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
				self.postback_handler.handle(data, sender)

	def _setup_fb_user_if_needed(self, sender):
		if self.bot.user is None:
			self.bot.setup_facebook_user(sender)

	def _handle_message(self, data, sender):
		message = data.text
		self.wit_client.run_actions(session_id=sender, message=message)
