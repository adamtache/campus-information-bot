# -*- coding: utf-8 -*-

DATA_TYPE_MESSAGE = 'Message'
DATA_TYPE_POSTBACK = 'Postback'

class Callback(object):

	def __init__(self, sender, recipient, data, page_id, time):
		self.sender = sender
		self.recipient = recipient
		self.data = data # Array of Data
		self.page_id = page_id
		self.time = time


class InvalidCallback(Callback):
	pass


class Data(object):

	def __init__(self, data_type):
		self.data_type = data_type


class TextMessage(Data):

	def __init__(self, mid, text, attachment, quick_reply):
		super(TextMessage, self).__init__(DATA_TYPE_MESSAGE)
		self.mid = mid #message id
		self.text = text
		self.attachment = attachment
		self.quick_reply = quick_reply


class Postback(Data):

	def __init__(self, payload):
		super(Postback, self).__init__(DATA_TYPE_POSTBACK)
		self.payload = payload


class Attachment(object):

	def __init__(self, attachment_type, payload):
		self.attachment_type = attachment_type
		self.payload = payload

	def get_audio(self):
		if self.attachment_type is 'audio':
			return self._get_url_from_payload()
		return ''

	def get_image(self):
		if self.attachment_type is 'image':
			return self._get_url_from_payload()
		return ''

	def get_video(self):
		if self.attachment_type is 'video':
			return self._get_url_from_payload()
		return ''

	def get_file(self):
		if self.attachment_type is 'file':
			return self._get_url_from_payload()
		return ''

	def _get_url_from_payload(self):
		if self.payload is None:
			return ''
		return self.payload.get('url')

	def get_location(self):
		if self.attachment_type is 'location':
			if self.payload is None:
				return ''
			coordinates = payload.get('coordinates')
			if coordinates is None:
				return ''
			return coordinates['lat'], coordinates['long']
		return ''


class QuickReply(object):

	def __init__(self, payload=None):
		self.payload = payload


def parse(data):
	if _is_invalid_data(data):
		return InvalidData()
	return _get_callback(data)

def _is_invalid_data(data):
	return data['object'] != 'page'

def _get_callback(data):
	sender = ''
	callback_data = []
	page_id = ''
	time = ''

	entry = data['entry']
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
	return Callback(sender, recipient, callback_data, page_id, time)

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
