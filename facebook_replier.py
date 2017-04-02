import json
import logging
import urllib

from google.appengine.api import urlfetch

ACCESS_TOKEN = "EAAGAoXpiPKIBAAsHJhD3k78TPUuACP0xh1zgnDkB6FPYkB8ZCSZAXV7fBdMYN07ZAXqS9wfMPZB06uSlmUTeZB6yW4vCeZAFxNkitPqf6BKZBosNWCBjZA2P1UdDZC8CcjdVlcYzZClG164rINr4MVGQ5DgenZAMhUdT59pIZBlKqrqZANQZDZD"
FACEBOOK_REPLY_URL =  "https://graph.facebook.com/v2.6/me/messages?"

def reply(recipient_id, message):
	params = _get_params(ACCESS_TOKEN)
	headers = _get_headers()
	payload = _get_payload(recipient_id, message)
	_post_reply(params, headers, payload)

def _post_reply(params, headers, payload):
	url = FACEBOOK_REPLY_URL + urllib.urlencode(params)
	try:
		request = urlfetch.fetch(
			url=url,
			payload=payload,
			method=urlfetch.POST,
			headers=headers,
		)
		logging.debug(request.content)
	except urlfetch.Error as e:
		logging.error(e.message)

def _get_params(access_token):
	return {
		"access_token": ACCESS_TOKEN
	}

def _get_payload(recipient_id, message):
	return json.dumps({
		"recipient": {
			"id": recipient_id
		},
		"message": {
			"text": message
		}
	})

def _get_headers():
	return {
		"Content-Type": "application/json"
	}
