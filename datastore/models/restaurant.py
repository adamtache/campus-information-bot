# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
from restaurant_availability import RestaurantAvailability

class Restaurant(ndb.Model):
	name = ndb.StringProperty()
	availabilities = ndb.StructuredProperty(RestaurantAvailability, repeated=True)
