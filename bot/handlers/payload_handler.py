# -*- coding: utf-8 -*-
from util.constants.facebook import GET_STARTED_PAYLOAD, RESTAURANT_AVAILABILITIES_PAYLOAD, RESTAURANT_AVAILABILITIES_RESPONSE

class PostbackHandler(object):

	def __init__(self, bot):
		self.bot = bot

	def handle(self, postback, sender):
		payload = postback.payload
		if payload == GET_STARTED_PAYLOAD:
			self._handle_get_started(sender)
		elif payload == RESTAURANT_AVAILABILITIES_PAYLOAD:
			self._handle_restaurant_availabilities(sender)
	
	def _handle_get_started(self, sender):
		self.bot.reply_welcome(sender)

	def _handle_restaurant_availabilities(self, sender):
		self.bot.reply_with(sender, RESTAURANT_AVAILABILITIES_RESPONSE)
