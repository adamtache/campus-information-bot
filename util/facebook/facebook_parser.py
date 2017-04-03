# -*- coding: utf-8 -*-

def parse(data):
	messaging_data = _get_entry_messaging_data(data)
	sender = _get_sender(messaging_data)
	message = _get_message(messaging_data)
	return sender, message

def _get_entry_messaging_data(data):
	return data['entry'][0]['messaging'][0]

def _get_sender(messaging_data):
	return messaging_data['sender']['id']

def _get_message(messaging_data):
	return messaging_data['message']['text']
