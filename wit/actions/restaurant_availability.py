# -*- coding: utf-8 -*-
from datetime import datetime
from util import datetime_util
from wit_actions import get_context_and_entities
from wit_actions import get_first_entity_value

restaurant_key = 'local_search_query'
datetime_key = 'datetime'
datetime_context_key = 'datetime'
restaurant_context_key = 'restaurant'
availability_key = 'restaurant_availability'
missing_restaurant_key = 'missing_restaurant'
missing_datetime_key = 'missing_datetime'

def get_restaurant_availability(request):
	"""Returns context, for which wit.ai uses to respond to the user."""
	context, entities = get_context_and_entities(request)
	return _get_updated_context(context, entities)

def _get_updated_context(context, entities):
	restaurant_raw = get_first_entity_value(entities, restaurant_key)
	datetime_raw = get_first_entity_value(entities, datetime_key)
	if restaurant_raw and datetime_raw:
		return _updated_context_using_restaurant_and_datetime(
			context, 
			restaurant_raw, 
			datetime_raw,
		)
	elif restaurant_raw:
		return _updated_context_using_restaurant_and_datetime(context, restaurant_raw)
	elif datetime_raw:
		return _updated_context_restaurant_missing_and_datetime_found(context)
	return _updated_context_restaurant_and_datetime_missing(context)

def _updated_context_using_restaurant_and_datetime(context, restaurant_raw, datetime_raw=None):
	restaurant = _find_closest_restaurant_in_db(restaurant_raw)
	return _updated_context_with_restaurant_availability(context, restaurant, datetime_raw)

def _updated_context_with_restaurant_availability(context, restaurant, datetime_raw):
	datetime = _get_datetime_localized_to_east_coast(datetime_raw)
	context[availability_key] = _calculated_restaurant_availability(
		restaurant,
		datetime,
	)
	context[restaurant_context_key] = restaurant
	context[datetime_context_key] = datetime_util.get_readable_datetime_string(datetime)
	return context

def _get_datetime_localized_to_east_coast(datetime_raw):
	if datetime_raw is None:
		return datetime_util.get_datetime_now_usa_east_coast()
	datetime = datetime_util.unicode_to_datetime(datetime_raw)
	return datetime_util.get_datetime_localized_to_east_coast(datetime)

def _updated_context_restaurant_missing_and_datetime_found(context):
	context['missing_restaurant'] = True
	return context

def _updated_context_restaurant_and_datetime_missing(context):
	context['missing_restaurant'] = True
	context['missing_datetime'] = True
	return context

def _find_closest_restaurant_in_db(restaurant_raw):
	return restaurant_raw

def _calculated_restaurant_availability(restaurant, datetime):
	"""Returns availability of restaurant at datetime."""
	return "open"
