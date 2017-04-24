# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class Availability(ndb.Model):
	date = ndb.DateProperty()
	opens_at = ndb.DateTimeProperty()
	closes_at = ndb.DateTimeProperty()
	location = ndb.StringProperty()
