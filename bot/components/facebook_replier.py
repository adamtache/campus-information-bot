import json

from requestor import Requestor

FACEBOOK_REPLY_URL =  "https://graph.facebook.com/v2.6/me/messages?"

class Replier(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(FACEBOOK_REPLY_URL)

	def reply_to(self, recipient_id, message):
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload(recipient_id, message)
		self.requestor.post(params, headers, payload)

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
