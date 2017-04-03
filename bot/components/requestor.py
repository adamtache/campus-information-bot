# -*- coding: utf-8 -*-
import json
import logging
import urllib

from google.appengine.api import urlfetch

get_request = urlfetch.GET
post_request = urlfetch.POST

class Requestor(object):

	def __init__(self, request_url):
		self.request_url = request_url

	def post(self, params, headers, payload):
		url = self._get_url(params)
		self._post_request(url, headers, payload)

	def get(self, params, headers):
		url = self._get_url(params)
		self._get_request(url, headers)

	def _get_url(self, params):
		return self.request_url + urllib.urlencode(params)

	def _post_request(self, url, headers, payload):
		try:
			result = urlfetch.fetch(
				url=url,
				payload=payload,
				method=post_request,
				headers=headers,
			)
			logging.debug(result.content)
		except urlfetch.Error as e:
			logging.error(e.message)

	def _get_request(self, url, headers):
		try:
			result = urlfetch.fetch(
				url=url,
				method=get_request,
				headers=headers,
			)
			logging.debug(result.content)
		except urlfetch.Error as e:
			logging.error(e.message)
