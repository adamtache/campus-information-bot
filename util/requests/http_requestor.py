# -*- coding: utf-8 -*-
import logging

from google.appengine.api import urlfetch

get_request = urlfetch.GET
post_request = urlfetch.POST

def post(url, headers, payload):
	try:
		result = urlfetch.fetch(
			url=url,
			payload=payload,
			method=post_request,
			headers=headers,
		)
		logging.debug(result.content)
		return result.content
	except urlfetch.Error as e:
		logging.error(e.message)

def get(url):
	try:
		result = urlfetch.fetch(url=url, method=get_request)
		return result.content
	except urlfetch.Error as e:
		logging.error(e.message)
