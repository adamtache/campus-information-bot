# -*- coding: utf-8 -*-
import re
from bot.requestors import facebook_replier
from restaurant_availability import get_restaurant_availability

def get_actions(replier):
	return {
		'send': replier.wit_send,
		'get_restaurant_availability': get_restaurant_availability,
	}
