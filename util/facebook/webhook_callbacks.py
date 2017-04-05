# -*- coding: utf-8 -*-
class WebhookCallback(object):

	def __init__(self, sender, recipient, data, page_id, time):
		self.sender = sender
		self.recipient = recipient
		self.data = data # Array of Data
		self.page_id = page_id
		self.time = time


class InvalidWebhookCallback(WebhookCallback):
	pass
