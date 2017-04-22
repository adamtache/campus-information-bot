# -*- coding: utf-8 -*-
import json

from requestor import Requestor
from util.constants.facebook import GET_STARTED_BUTTON_URL, GET_STARTED_PAYLOAD

class GetStartedButton(object):

	def __init__(self, access_token):
		self.access_token = access_token
		self.requestor = Requestor(GET_STARTED_BUTTON_URL)

	def setup(self):
		params = self._get_params()
		headers = self._get_headers()
		payload = self._get_payload()
		self.requestor.post(params, headers, payload)

	def _get_headers(self):
		return {
			"Content-Type": "application/json"
		}

	def _get_params(self):
		return {
			"access_token": self.access_token
		}

	def _get_GET_params(self):
		return {
			"access_token": self.access_token,
			"fields": "get_started"
		}

	def _get_payload(self):
		return json.dumps({
			"get_started": {
				"payload": GET_STARTED_PAYLOAD
			}
		})
