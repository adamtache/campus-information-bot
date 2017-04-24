# -*- coding: utf-8 -*-

class Availability(object):

	def __init__(self, date, opens_at, closes_at, location=None):
		self.date = date
		self.opens_at = opens_at
		self.closes_at = closes_at
		self.location = location

	def is_closed_for_date(self):
		return opens_at is None or closes_at is None

	def __str__(self):
		return self.opens_at.__str__() + " " + self.closes_at.__str__() + " on " + self.date.__str__()

	__repr__ = __str__
