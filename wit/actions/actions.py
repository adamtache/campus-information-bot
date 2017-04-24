# -*- coding: utf-8 -*-
import re
from bot.requestors import facebook_replier
from schedule_availability import get_schedule_availability

def get_actions(replier):
	return {
		'send': replier.wit_send,
		'get_schedule_availability': get_schedule_availability,
	}
