# -*- coding: utf-8 -*-
from models.user import User
from requestors.facebook_get_started_button import GetStartedButton
from requestors.facebook_greeter import Greeter
from requestors.facebook_menu import Menu
from requestors.facebook_replier import Replier
from requestors.facebook_user import FacebookUserRequestor

ACCESS_TOKEN = "EAAGAoXpiPKIBADJl5MoELaDPr0K3n1UaXwZAJaJ2RFPueK9OWMopPOWNLI1hzhFhCWMEhgZCmcqVuZAyNIsfsABOh8R6fLThZBNLkyDyXpGOUvd1cJrBbFoa7bcGIwyPUUZBWswgsddHIruU2WrorQ4pDdgubF0i0ZCbEcKZASO0gZDZD"

class CampusBot(object):

	def __init__(self):
		self.access_token = ACCESS_TOKEN
		self._create_components()
		self._setup_components()

	def reply_to(self, sender, message):
		self.replier.reply_to(sender, message)

	def setup_facebook_user(self, sender):
		"""User info only available after a person has sent a message
		to bot or clicked the "Send to Messenger" plugin"""
		if self.user is not None:
			return
		user_requestor = FacebookUserRequestor(self.access_token, sender)
		user_json = user_requestor.get_user_json()
		self._setup_user(user_json)

	def _create_components(self):
		self.replier = Replier(ACCESS_TOKEN)
		self.greeter = Greeter(ACCESS_TOKEN)
		self.get_started_button = GetStartedButton(ACCESS_TOKEN)
		self.menu = Menu(ACCESS_TOKEN)
		self.user = None # User info not accessible via API until first interaction

	def _setup_components(self):
		self.get_started_button.setup()
		self.menu.setup()

	def _setup_user(self, user_json):
		facebook_user = User(user_json)
		self.user = facebook_user
		self._setup_greeter()

	def _setup_greeter(self):
		self.greeter.setup(self.user)
