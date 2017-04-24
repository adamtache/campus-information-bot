# -*- coding: utf-8 -*-
from availability import Availability
from google.appengine.ext import ndb

class Schedule(ndb.Model):
	name = ndb.StringProperty()
	availabilities = ndb.StructuredProperty(Availability, repeated=True)
