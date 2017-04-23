# -*- coding: utf-8 -*-
from datastore.models.restaurants.restaurant import Restaurant

def get_restaurant(restaurant_name):
	return Restaurant.query(Restaurant.name == restaurant_name)

def get_all_restaurants():
	q = Restaurant.query().order(-Restaurant.name)
	restaurants = []
	for restaurant in q:
		restaurants.append(restaurant)
	return restaurants
