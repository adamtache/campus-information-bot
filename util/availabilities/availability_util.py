# -*- coding: utf-8 -*-
from util import datetime_util

CLOSED = 'closed'
OPEN = 'open'

def get_readable_availabilities(availabilities):
	avail_string = ''
	for avail in availabilities:
		opens_at = avail.opens_at
		closes_at = avail.closes_at
		avail_string += datetime_util.get_readable_time(opens_at) + (
			" to " + datetime_util.get_readable_time(closes_at) + "\n"
		)
	avail_string = avail_string if avail_string is not None else 'Never'
	return avail_string

def get_open_or_closed(availabilities):
	for avail in availabilities:
		if avail.opens_at is not None or avail.closes_at is not None:
			return OPEN
	return CLOSED

def has_any_availabilities(availabilities):
	open_or_closed = get_open_or_closed(availabilities)
	if open_or_closed == OPEN:
		return True
	return False

def get_last_date_available(availabilities):
	if not availabilities:
		return None
	return availabilities[-1].date
