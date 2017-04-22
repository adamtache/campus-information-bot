# -*- coding: utf-8 -*-
import json

from requestor import Requestor
from util.constants.facebook import REPLY_URL, WELCOME_TEXT

class Replier(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(REPLY_URL)

	def wit_send(self, request, response):
		recipient_id = request['session_id']
		message = response['text']
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, message)
		self.requestor.post(params, headers, payload)

	def reply_with(self, recipient_id, message):
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, message)
		self.requestor.post(params, headers, payload)

	def reply_welcome(self, recipient_id, user):
		text = self._get_welcome_text(user)
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, text)
		self.requestor.post(params, headers, payload)

	def _get_welcome_text(self, user):
		return "Hi " + user.first_name + " " + user.last_name + ". " + WELCOME_TEXT

	def _get_params(self):
		return {
			"access_token": self.access_token
		}

	def _get_headers(self):
		return {
			"Content-Type": "application/json"
		}

	def _get_payload(self, recipient_id, message):
		return json.dumps({
			"recipient": {
				"id": recipient_id
			},
			"message": {
				"text": message
			}
		})
