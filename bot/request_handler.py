# -*- coding: utf-8 -*-
from util.facebook import facebook_parser

class RequestHandler(object):

	def __init__(self, bot):
		self.bot = bot
		self.bot.start()

	def handle(self, request):
		sender, message = facebook_parser.parse(request.json)
		self._setup_fb_user_if_needed(sender)
		self.bot.reply_to(sender, message)

	def _setup_fb_user_if_needed(self, sender):
		if self.bot.user is None:
			self.bot.setup_facebook_user(sender)
