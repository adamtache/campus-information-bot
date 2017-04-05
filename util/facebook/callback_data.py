# -*- coding: utf-8 -*-

DATA_TYPE_MESSAGE = 'Message'
DATA_TYPE_POSTBACK = 'Postback'

class CallbackData(object):

	def __init__(self, data_type):
		self.data_type = data_type


class TextMessage(CallbackData):

	def __init__(self, mid, text, attachment, quick_reply):
		super(TextMessage, self).__init__(DATA_TYPE_MESSAGE)
		self.mid = mid #message id
		self.text = text
		self.attachment = attachment
		self.quick_reply = quick_reply


class Postback(CallbackData):

	def __init__(self, payload):
		super(Postback, self).__init__(DATA_TYPE_POSTBACK)
		self.payload = payload
