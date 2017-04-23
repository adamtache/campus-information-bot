# -*- coding: utf-8 -*-
from datastore.util.restaurants import restaurants_handler
from datetime import datetime
from util import datetime_util
from util.restaurants import similarity
from util.restaurants import availability_checker
from wit_actions import get_context_and_entities
from wit_actions import get_first_entity_value

availability_key = 'restaurant_availability'
datetime_context_key = 'datetime'
datetime_key = 'datetime'
missing_restaurant_key = 'missing_restaurant'
restaurant_key = 'local_search_query'
restaurant_context_key = 'restaurant'
restaurant_error_key = 'restaurant_error'

def get_restaurant_availability(request):
	"""Returns context, for which wit.ai uses to respond to the user."""
	context, entities = get_context_and_entities(request)
	return _get_updated_context(context, entities)

def _get_updated_context(context, entities):
	restaurant_raw = get_first_entity_value(entities, restaurant_key)
	datetime_raw = get_first_entity_value(entities, datetime_key)
	if restaurant_raw:
		return _updated_context_using_restaurant_and_datetime(
			context,
			restaurant_raw,
			datetime_raw,
		)
	context[missing_restaurant_key] = True
	return context

def _updated_context_using_restaurant_and_datetime(context, restaurant_raw, datetime_raw):
	restaurant = similarity.get_closest_match(
		restaurant_raw, 
		restaurants_handler.get_all_restaurants(),
	)
	if restaurant is None:
		return _updated_context_with_no_restaurant_match_found(context)
	datetime = _get_datetime(datetime_raw)
	return _updated_context_with_restaurant_availability(context, restaurant, datetime)

def _get_datetime(datetime_raw):
	if datetime_raw is None:
		return datetime_util.get_datetime_localized_to_east_coast(datetime.now())
	return datetime_util.unicode_to_datetime(datetime_raw)

def _updated_context_with_restaurant_availability(context, restaurant, datetime):
	context[availability_key] = availability_checker.get_availability_east_coast(restaurant, datetime)
	context[restaurant_context_key] = restaurant.name
	context[datetime_context_key] = datetime_util.get_readable_datetime_string(datetime)
	return context

def _updated_context_with_no_restaurant_match_found(context):
	context[restaurant_error_key] = True
	return context
