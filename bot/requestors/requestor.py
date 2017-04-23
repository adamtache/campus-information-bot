# -*- coding: utf-8 -*-
import json
import urllib

from util.requests import http_requestor

class Requestor(object):

	def __init__(self, request_url):
		self.request_url = request_url

	def post(self, params, headers, payload):
		url = self._get_url(params)
		return http_requestor.post(url, headers, payload)

	def get(self, params, headers=None):
		url = self._get_url(params)
		return http_requestor.get(url)

	def _get_url(self, params):
		return self.request_url + urllib.urlencode(params)
