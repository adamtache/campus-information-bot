# -*- coding: utf-8 -*-

class Schedule(object):

	def __init__(self, name, availabilities, location=None):
		self.name = name
		self.availabilities = availabilities

	def add_availability(self, availability):
		if self.availabilities is None:
			self.availabilities = []
		self.availabilities.append(availability)

	def __str__(self):
		avails = ''
		for avail in self.availabilities:
			avails = avails + "\n" + avail.__str__()
		return self.name + " " + avails
