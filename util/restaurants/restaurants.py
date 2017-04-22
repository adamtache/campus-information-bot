# -*- coding: utf-8 -*-

class Restaurant(object):

	def __init__(self, name, availabilities_this_week):
		self.name = name
		self.availabilities_this_week = availabilities_this_week

	def __str__(self):
		avails = ''
		for avail in self.availabilities_this_week:
			avails = avails + "\n" + avail.__str__()
		return self.name + " " + avails

class RestaurantAvailability(object):

	def __init__(self, date, opens_at, closes_at):
		self.date = date
		self.opens_at = opens_at
		self.closes_at = closes_at

	def is_closed_for_date(self):
		return opens_at is None or closes_at is None

	def __str__(self):
		return self.opens_at.__str__() + " " + self.closes_at.__str__() + " on " + self.date.__str__()

	__repr__ = __str__
