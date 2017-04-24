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
