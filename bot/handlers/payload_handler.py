# -*- coding: utf-8 -*-
from util.constants.facebook import GET_STARTED_PAYLOAD, AVAILABILITIES_PAYLOAD, AVAILABILITIES_RESPONSE, HOURS_PAYLOAD, HOURS_RESPONSE

class PostbackHandler(object):

	def __init__(self, bot):
		self.bot = bot

	def handle(self, postback, sender):
		payload = postback.payload
		if payload == GET_STARTED_PAYLOAD:
			self.bot.reply_welcome(sender)
		elif payload == AVAILABILITIES_PAYLOAD:
			self.bot.reply_with(sender, AVAILABILITIES_RESPONSE)
		elif payload == HOURS_PAYLOAD:
			self.bot.reply_with(sender, HOURS_RESPONSE)
