# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import parser
from pytz import timezone

def unicode_to_datetime(datetime_unicode):
	return parser.parse(datetime_unicode)

def get_datetime_now_usa_east_coast():
	east_coast = timezone('US/Eastern')
	return datetime.now(east_coast)

def get_datetime_localized_to_east_coast(datetime):
	tzinfo = datetime.tzinfo
	if tzinfo is None:
		return datetime
	return datetime

def get_readable_datetime_string(datetime):
	return datetime.strftime("%B %d, %Y at %I:%M%p")

def datetime_with_current_year(datetime):
	return datetime.replace(year=datetime.today().year)
