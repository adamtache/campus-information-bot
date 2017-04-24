# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

class Event(ndb.Model):
	name = ndb.StringProperty()
	location = ndb.StringProperty()
	start = ndb.DateTimeProperty()
	end = ndb.DateTimeProperty()
