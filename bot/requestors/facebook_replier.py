# -*- coding: utf-8 -*-
import json

from requestor import Requestor

FACEBOOK_REPLY_URL =  "https://graph.facebook.com/v2.6/me/messages?"

class Replier(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(FACEBOOK_REPLY_URL)

	def wit_send(self, request, response):
		recipient_id = request['session_id']
		message = response['text']
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, message)
		self.requestor.post(params, headers, payload)

	def reply_to(self, recipient_id, message, user):
		text = message.text + " " + user.first_name + " " + user.last_name
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, text)
		self.requestor.post(params, headers, payload)

	def reply_welcome(self, recipient_id, user):
		text = self._get_welcome_text(user)
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, text)
		self.requestor.post(params, headers, payload)

	def _get_welcome_text(self, user):
		return "Hi " + user.first_name + " " + user.last_name + ". I'm so glad you decided to activate me. You can send a message or access my menu below. Have fun :)"

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
