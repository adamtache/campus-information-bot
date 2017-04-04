# -*- coding: utf-8 -*-
import json

from requestor import Requestor

FACEBOOK_USER_URL = "https://graph.facebook.com/v2.6/"

class FacebookUserRequestor(object):

	def __init__(self, access_token, user_id):
		self.access_token = access_token
		self.requestor = Requestor(self._get_url(user_id))

	def _get_url(self, user_id):
		return FACEBOOK_USER_URL + user_id + "?"

	def get_user_json(self):
		params = self._get_params()
		headers = self._get_headers()
		return self.requestor.get(params)

	def _get_params(self):
		return {
			"access_token": self.access_token,
			"fields": self._get_fields()
		}

	def _get_fields(self):
		fields = [
			"first_name",
			"last_name",
			"locale",
			"timezone",
		]
		return self._get_formatted_fields(fields)

	def _get_formatted_fields(self, fields):
		return ",".join(fields)

	def _get_headers(self):
		return {
			"Content-Type": "application/json"
		}
