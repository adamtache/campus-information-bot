# -*- coding: utf-8 -*-
import json

from util import datetime_util

class Event(object):

	def __init__(self, raw_event):
		event_json = None
		try:
			event_json = json.loads(raw_event)
		except ValueError:
			pass
		self.name = event_json.get('summary')
		self.location = event_json.get('location')
		self.start = self._get_start_datetime(event_json)
		self.end = self._get_end_datetime(event_json)

	def _get_start_datetime(self, event_json):
		return self._extract_datetime(event_json, 'start')

	def _get_end_datetime(self, event_json):
		return self._extract_datetime(event_json, 'end')

	def _extract_datetime(self, event_json, event_key):
		start = event_json.get(event_key)
		if start is None:
			return
		start_datetime = start.get('dateTime')
		if start_datetime is None:
			return
		return datetime_util.unicode_to_datetime(start_datetime)
