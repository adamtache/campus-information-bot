# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser
from pytz import timezone, utc

DATETIME_STRING_ERROR = 'Did not provide valid datetime string'

def unicode_to_datetime(datetime_unicode):
	return parser.parse(datetime_unicode)

def get_datetime_now_usa_east_coast():
	return datetime.now(timezone('US/Eastern'))

def get_datetime_localized_to_east_coast(datetime):
	if datetime is None:
		return None
	return timezone('US/Eastern').localize(datetime)

def get_readable_datetime_string(datetime):
	if datetime is None:
		raise ValueError(DATETIME_STRING_ERROR)
	return datetime.strftime("%B %d, %Y at %I:%M %p")

def get_readable_date(datetime):
	if datetime is None:
		raise ValueError(DATETIME_STRING_ERROR)
	return datetime.strftime("%B %d")

def get_readable_time(datetime):
	if datetime is None:
		raise ValueError(DATETIME_STRING_ERROR)
	return datetime.strftime("%I:%M %p")

def datetime_with_current_year(datetime):
	if datetime is None:
		raise ValueError('Did not provide valid datetime string')
	return datetime.replace(year=datetime.today().year)

def are_same_date(datetime1, datetime2):
	return datetime1.date() == datetime2.date()

def is_midnight(datetime):
	seconds_since_midnight = (datetime - datetime.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	return seconds_since_midnight == 0
