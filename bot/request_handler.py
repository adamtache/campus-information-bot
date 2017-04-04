# -*- coding: utf-8 -*-
from util.facebook.facebook_parser import parse
from util.facebook.facebook_parser import InvalidCallback
from util.facebook.facebook_parser import Callback
from util.facebook.facebook_parser import DATA_TYPE_MESSAGE
from util.facebook.facebook_parser import DATA_TYPE_POSTBACK

class RequestHandler(object):

	def __init__(self, bot):
		self.bot = bot

	def handle(self, request):
		callback = parse(request.json)
		if type(callback) is InvalidCallback:
			return "ok", 200
		self._handle_callback(callback)
		# Must send back 200 to facebook within 20 seconds
		return "ok", 200

	def _handle_callback(self, callback):
		sender = callback.sender
		# self._setup_fb_user_if_needed(sender)
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
		self.bot.reply_to(sender, message)

	def _handle_postback(self, postback, sender):
		pass
