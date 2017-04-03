# -*- coding: utf-8 -*-
from models.user import User
from requestors.facebook_get_started_button import GetStartedButton
from requestors.facebook_greeter import Greeter
from requestors.facebook_menu import Menu
from requestors.facebook_replier import Replier
from requestors.facebook_user import FacebookUserRequestor

ACCESS_TOKEN = "EAAGAoXpiPKIBAKYXpZAeAPi2Br4byjeFibinY4j3ZANvqOUwNggGvnRLIIu7uyfab5MEiOeSqiGeZBe0E6va4DTCaY38oR1p922VsYRsdTeiey5QBkJfM7XJAsnYObZAWaET1HXidQqmnlHJr5WhQ6ZAm9ps7Cudx8bAfHNdSbwZDZD"

class CampusBot(object):

	def __init__(self):
		self.access_token = ACCESS_TOKEN

	def start(self):
		self._create_components()
		self._setup_components()

	def reply_to(self, sender, message):
		self.replier.reply_to(sender, message)

	def setup_facebook_user(self, sender):
		"""User info only available after a person has sent a message
		to bot or clicked the "Send to Messenger" plugin"""
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
