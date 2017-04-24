# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
from datastore.models.availability import Availability

class Restaurant(ndb.Model):
	name = ndb.StringProperty()
	availabilities = ndb.StructuredProperty(Availability, repeated=True)
