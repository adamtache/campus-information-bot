# -*- coding: utf-8 -*-
from util.datetime_util import are_same_date
from util.datetime_util import get_datetime_localized_to_east_coast
from util.datetime_util import get_readable_date

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
		last_date_available_string = _get_last_date_available(availabilities)
		if last_date_available_string is None:
			return UNKNOWN
		else:
			return last_date_available_string
	return CLOSED

def _information_not_available_for_datetime(datetime, availabilities):
	if availabilities is None:
		return True
	return datetime.date() > availabilities[-1].date

def _get_last_date_available(availabilities):
	last_date = availabilities[-1].date
	if last_date is None:
		None
	month_and_day = get_readable_date(last_date)
	return UNKNOWN + " (information not available past " + month_and_day + ")"
