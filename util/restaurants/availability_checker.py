# -*- coding: utf-8 -*-
from util import availability_util
from util.datetime_util import are_same_date
from util.datetime_util import get_datetime_localized_to_east_coast

CLOSED = "closed"
OPEN = "open"
UNKNOWN = "unknown to be open or closed"

def get_availability_east_coast(restaurant, datetime):
	"""Returns availability of restaurant at datetime."""
	availabilities = restaurant.availabilities
	for avail in availabilities:
		# ndb on GAE only supports UTC and can't handle timezone aware datetimes
		opens_at = get_datetime_localized_to_east_coast(avail.opens_at)
		closes_at = get_datetime_localized_to_east_coast(avail.closes_at)
		if opens_at is None or closes_at is None:
			continue
		elif datetime < opens_at:
			return CLOSED
		elif datetime >= opens_at and datetime <= closes_at:
			return OPEN
	if _information_not_available_for_datetime(datetime, availabilities):
		last_date_available_string = _get_last_date_available_string(availabilities)
		if last_date_available_string is None:
			return UNKNOWN
		else:
			return last_date_available_string
	return CLOSED

def get_availabilities(restaurant, date):
	availabilities = []
	for avail in restaurant.availabilities:
		opens_at = avail.opens_at
		if opens_at is None:
			continue
		if opens_at.date() == date:
			availabilities.append(avail)
	return availabilities

def _information_not_available_for_datetime(datetime, availabilities):
	if availabilities is None:
		return True
	return datetime.date() > availabilities[-1].date

def _get_last_date_available_string(availabilities):
	if availabilities is None:
		return None
	last_date = availability_util.get_last_date_available(availabilities)
	return UNKNOWN + " (information not available past " + \
		datetime_util.get_readable_date(last_date) + ")"
