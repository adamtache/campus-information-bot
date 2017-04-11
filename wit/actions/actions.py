# -*- coding: utf-8 -*-
import re

def get_actions():
	return {
		'send': send,
	}

def send(request, response):
    fb_id = request['session_id']
    text = response['text']
