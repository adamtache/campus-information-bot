# -*- coding: utf-8 -*-
import webapp2

from datastore.models.restaurants.restaurant import Restaurant
from datastore.models.restaurants.restaurant_availability import RestaurantAvailability
from google.appengine.ext import ndb
from util.restaurants.restaurant_scraper import RestaurantScraper

DEFAULT_RESTAURANTS_NAME = 'default_restaurants'

def get_restaurant(restaurant_name):
	return Restaurant.query(Restaurant.name == restaurant_name)

def get_all_restaurants():
	q = Restaurant.query().order(-Restaurant.name)
	restaurants = []
	for restaurant in q:
		restaurants.append(restaurant)
	return restaurants

def post():
	for restaurant in RestaurantScraper().get_restaurants():
		_post_restaurant_to_db(restaurant)

def _post_restaurant_to_db(restaurant_to_post):
	parent = _get_restaurant_key(DEFAULT_RESTAURANTS_NAME)
	name = restaurant_to_post.name
	availabilities = _converted_availabilities_for_datastore(
		restaurant_to_post.availabilities_this_week,
	)
	restaurant = Restaurant(parent=parent, name=name, availabilities=availabilities)
	restaurant.put()

def _get_restaurants_name():
	return DEFAULT_RESTAURANTS_NAME

def _get_restaurant_key(restaurants_name=DEFAULT_RESTAURANTS_NAME):
	"""Constructs a Datastore key for Restaurants entity.

	Uses restaurants_name as the key.
	"""
	return ndb.Key('Restaurants', restaurants_name)

def _converted_availabilities_for_datastore(availabilities_this_week):
	avails = []
	for availabilities in availabilities_this_week:
		for availability in availabilities:
			avails.append(_get_availability_for_datastore(availability))
	return avails

def _get_availability_for_datastore(availability):
	return RestaurantAvailability(
		date=availability.date,
		opens_at=availability.opens_at,
		closes_at=availability.closes_at,
	)
