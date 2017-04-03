# -*- coding: utf-8 -*-
from components.facebook_greeter import Greeter
from components.facebook_replier import Replier

ACCESS_TOKEN = "EAAGAoXpiPKIBAP8f5C4WwSHtigeJ3pYYtEZBvSXO0iqHlGzzRrA5XdhFYfBVgwnAOzAtZAFEtEZBI3ZAErrGobXvZADTvz7ZAYg8SqXD4RPUHHFaflVZAQzXAdvmJr0wQc0HPaVAUH0lsBxV6nsJOoeEgmp7cy9Oza9jHJhD8vQHAZDZD"

class CampusBot(object):

	def __init__(self):
		self.replier = Replier(ACCESS_TOKEN)
		self.greeter = Greeter(ACCESS_TOKEN)
		self.setup()

	def setup(self):
		self.greeter.setup()

	def handle(self, sender, message):
		self.replier.reply_to(sender, message)
