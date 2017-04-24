# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from models.availability import Availability
from models.schedule import Schedule
from scraper import Scraper
from util import datetime_util
from util.google_calendar.client import get_events_from_calendar

FOOD_TRUCK_CALENDAR_ID = 'vgkckpl2e04dgvbtn94u1jeuk0@group.calendar.google.com'

class FoodTruckScraper(Scraper):

	def get_schedules(self):
		now = datetime.utcnow()
		raw_events = get_events_from_calendar(
			calendar_id=FOOD_TRUCK_CALENDAR_ID, 
			time_min=now.isoformat() + 'Z',
			time_max=(now + timedelta(days=20)).isoformat() + 'Z',
			single_events=True, 
			order_by='startTime',
		)
		return self._create_schedules(raw_events)

	def _create_schedules(self, raw_events):
		schedules_dict = {} # name to schedule object
		for event_json in raw_events:
			name = event_json.get('summary')
			location = event_json.get('location')
			opens_at = self._extract_datetime(event_json, 'start')
			closes_at = self._extract_datetime(event_json, 'end')
			date = opens_at.date() if opens_at is not None else None
			availability = Availability(
				date=date,
				opens_at=opens_at,
				closes_at=closes_at,
				location=location,
			)
			if name in schedules_dict:
				schedules_dict[name].add_availability(availability)
			else:
				schedules_dict[name] = Schedule(
					name=name,
					availabilities=[availability],
				)
		return schedules_dict.values()

	def _extract_datetime(self, event_json, event_key):
		start = event_json.get(event_key)
		if start is None:
			return
		start_datetime = start.get('dateTime')
		if start_datetime is None:
			return
		return datetime_util.unicode_to_datetime(start_datetime)
