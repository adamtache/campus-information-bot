# -*- coding: utf-8 -*-
import re
from bot.requestors import facebook_replier

def get_actions(replier):
	return {
		'send': replier.wit_send,
	}
