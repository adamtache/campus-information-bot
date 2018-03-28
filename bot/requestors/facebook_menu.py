# -*- coding: utf-8 -*-
import json

from requestor import Requestor
from util.constants.facebook import AVAILABILITIES_PAYLOAD, HOURS_PAYLOAD, MENU_URL

class Menu(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(MENU_URL)

	def setup(self):
		self._make_post_request()

	def _make_post_request(self):
		"""Getting started button required to be POST'd first
		"""
		params = self._get_POST_params()
		headers = self._get_headers()
		payload = self._get_payload()
		self.requestor.post(params, headers, payload)

	def _get_headers(self):
		return {
			"Content-Type": "application/json"
		}

	def _get_POST_params(self):
		return {
			"access_token": self.access_token
		}

	def _get_GET_params(self):
		return {
			"access_token": self.access_token,
			"fields": "persistent_menu"
		}

	def _get_payload(self):
		return json.dumps({
			"persistent_menu": [
				{
					"locale": "default",
					"composer_input_disabled": False,
					"call_to_actions": [
						self._get_actions()
					]
				}
			]
		})

	def _get_actions(self):
		return {
			"title": "Menu",
			"type": "nested",
			"call_to_actions": self._get_menu_buttons()
		}

	def _get_menu_buttons(self):
		return [
			self._get_hours_button(),
			self._get_availabilities_button(),
		]

	def _get_hours_button(self):
		return {
			"title": "Hours",
			"type": "postback",
			"payload": HOURS_PAYLOAD
		}

	def _get_availabilities_button(self):
		return {
			"title": "Availabilities",
			"type": "postback",
			"payload": AVAILABILITIES_PAYLOAD
		}
