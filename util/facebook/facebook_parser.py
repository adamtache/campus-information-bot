# -*- coding: utf-8 -*-
from callback_data import TextMessage
from callback_data import Postback
from quick_reply import QuickReply
from messages import Attachment
from webhook_callbacks import InvalidWebhookCallback
from webhook_callbacks import WebhookCallback

def parse(data):
	if _is_invalid_data(data):
		return InvalidWebhookCallback()
	return _get_callback(data)

def _is_invalid_data(data):
	return data.get('object') != 'page'

def _get_callback(data):
	sender = ''
	callback_data = []
	page_id = ''
	time = ''

	entry = data.get('entry')
	for event in entry:
		page_id = event.get('id')
		time = event.get('time')
		messaging = event.get('messaging')
		for messaging_event in messaging:
			sender = messaging_event['sender']['id']
			recipient = messaging_event['recipient']['id']
			if 'message' in messaging_event:
				callback_data.append(_get_text_message(messaging_event))
			elif 'postback' in messaging_event:
				callback_data.append(_get_postback(messaging_event))
	return WebhookCallback(sender, recipient, callback_data, page_id, time)

def _get_text_message(messaging_event):
	message = messaging_event['message']

	mid = message['mid']
	text = message.get('text') or ''
	attachments = _get_attachments(message.get('attachments'))
	quick_reply = _get_quick_reply(message.get('quick_reply'))
	return TextMessage(mid, text, attachments, quick_reply)

def _get_postback(messaging_event):
	postback = messaging_event['postback']
	payload = postback['payload']
	return Postback(payload)

def _get_attachments(raw_attachments):
	if raw_attachments is None:
		return []
	attachments = []
	for attachment in raw_attachments:
		attachment_type = attachment['type']
		payload = attachment['payload']
		attachments.append(Attachment(attachment_type, payload))
	return attachments

def _get_quick_reply(quick_reply_dict):
	if quick_reply_dict is None:
		return QuickReply()
	payload = quick_reply_dict.get('payload')
	return QuickReply(payload)
