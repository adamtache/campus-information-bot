# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class RestaurantAvailability(ndb.Model):
	opens_at = ndb.DateTimeProperty()
	closes_at = ndb.DateTimeProperty()
