# -*- coding: utf-8 -*-
import json

from requestor import Requestor

FACEBOOK_GREETER_URL = "https://graph.facebook.com/v2.6/me/thread_settings"

class Greeter(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(FACEBOOK_GREETER_URL)

	def setup(self, user):
		self.user = user
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload()
		self.requestor.post(params, headers, payload)

	def _get_params(self):
		return {
			"access_token": self.access_token
		}

	def _get_headers(self):
		return {
			"Content-Type": "application/json"
		}

	def _get_payload(self):
		return json.dumps(
			{
				"greeting": [
					{
						"locale": "default",
						"text": self._get_greeting_text()
					}
				]
			}
		)

	def _get_greeting_text(self):
		return "Hello " + self.user.first_name + "! Welcome to Duke's campus chat bot. \
		See the menu for what I can do. Enjoy!"
