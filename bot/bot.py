# -*- coding: utf-8 -*-
from util.tokens import FACEBOOK_ACCESS_TOKEN
from models.user import User
from requestors.facebook_get_started_button import GetStartedButton
from requestors.facebook_greeter import Greeter
from requestors.facebook_menu import Menu
from requestors.facebook_replier import Replier
from requestors.facebook_user import FacebookUserRequestor

class Bot(object):

	def __init__(self):
		self.access_token = FACEBOOK_ACCESS_TOKEN
		self._create_components()
		self._setup_components()

	def reply_to(self, sender, message):
		self.replier.reply_to(sender, message, self.user)

	def reply_welcome(self, sender):
		self.replier.reply_welcome(sender, self.user)

	def setup_facebook_user(self, sender):
		"""User info only available after a person has sent a message
		to bot or clicked the "Send to Messenger" plugin"""
		if self.user is not None:
			return
		user_requestor = FacebookUserRequestor(self.access_token, sender)
		user_json = user_requestor.get_user_json()
		self._setup_user(user_json)

	def _create_components(self):
		self.replier = Replier(self.access_token)
		self.greeter = Greeter(self.access_token)
		self.get_started_button = GetStartedButton(self.access_token)
		self.menu = Menu(self.access_token)
		self.user = None # User info not accessible via API until first interaction

	def _setup_components(self):
		self.get_started_button.setup()
		self.greeter.setup()
		self.menu.setup()

	def _setup_user(self, user_json):
		facebook_user = User(user_json)
		self.user = facebook_user
