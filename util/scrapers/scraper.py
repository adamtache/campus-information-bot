# -*- coding: utf-8 -*-
import abc

class Scraper(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_schedules(self):
		"""Scrapes and returns Schedule objects"""
		return
