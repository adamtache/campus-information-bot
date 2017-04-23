# -*- coding: utf-8 -*-
from datetime import datetime
from util import availability_util
from util import datetime_util
from util.datastore import restaurants_util
from util.math.similarity import any_word_meets_threshold
from util.restaurants import availability_checker
from util.restaurants.similarity import get_closest_match
from wit_actions import get_context_and_entities
from wit_actions import get_first_entity_value

availability_key = 'restaurant_availability'
availabilities_key = 'availabilities'
datetime_context_key = 'datetime'
datetime_key = 'datetime'
information_not_available_for_that_day_key = 'not_available'
last_date_key = 'last_date'
missing_restaurant_key = 'missing_restaurant'
no_availabilities_found_key = 'no'
restaurant_key = 'local_search_query'
restaurant_context_key = 'restaurant'
restaurant_not_found = 'restaurant_error'

def get_restaurant_availability(request):
	"""Returns context, for which wit.ai uses to respond to the user."""
	context, entities = get_context_and_entities(request)
	return _get_updated_context(context, entities, request['text'])

def _get_updated_context(context, entities, user_text):
	restaurant_raw = get_first_entity_value(entities, restaurant_key)
	datetime_raw = get_first_entity_value(entities, datetime_key)
	if restaurant_raw:
		return _updated_context_using_restaurant_and_datetime(
			context,
			user_text,
			restaurant_raw,
			datetime_raw,
		)
	context[missing_restaurant_key] = True
	return context

def _updated_context_using_restaurant_and_datetime(context, user_text, restaurant_raw, datetime_raw):
	restaurant = get_closest_match(
		restaurant_raw,
		restaurants_util.get_all_restaurants(),
	)
	if restaurant is None:
		context[restaurant_not_found] = True
		return context
	datetime = _get_datetime(datetime_raw)
	if datetime_util.is_midnight(datetime) and _user_asked_for_availabilities_of_entire_day(user_text):
		return _updated_context_with_entire_day_availabilities(context, restaurant, datetime)
	return _updated_context_with_single_availability(context, restaurant, datetime)

def _user_asked_for_availabilities_of_entire_day(user_text):
	if any_word_meets_threshold(user_text, 'midnight', 0.75):
		return False
	return '12' not in user_text and '0:00' not in user_text

def _get_datetime(datetime_raw):
	if datetime_raw is None:
		return datetime_util.get_datetime_localized_to_east_coast(datetime.now())
	return datetime_util.unicode_to_datetime(datetime_raw)

def _updated_context_with_entire_day_availabilities(context, restaurant, datetime):
	availabilities = availability_checker.get_availabilities(
		restaurant, 
		datetime.date(),
	)
	context[restaurant_context_key] = restaurant.name
	if availability_util.has_any_availabilities(availabilities):
		context[availabilities_key] = availability_util.get_readable_availabilities(availabilities)
		return context
	last_date = availability_util.get_last_date_available(restaurant.availabilities)
	if last_date is None or datetime.date() <= last_date:
		context[no_availabilities_found_key] = True
		return context
	context[information_not_available_for_that_day_key] = True
	context[last_date_key] = datetime_util.get_readable_date(last_date)
	return context

def _updated_context_with_single_availability(context, restaurant, datetime):
	context[availability_key] = availability_checker.get_availability_east_coast(restaurant, datetime)
	context[restaurant_context_key] = restaurant.name
	context[datetime_context_key] = datetime_util.get_readable_datetime_string(datetime)
	return context
