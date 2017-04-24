# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from models.event import Event
from util.google_calendar.client import get_events_from_calendar

FOOD_TRUCK_CALENDAR_ID = 'vgkckpl2e04dgvbtn94u1jeuk0@group.calendar.google.com'

def get_events():
	now = datetime.now()
	raw_events = get_events_from_calendar(
		calendar_id=FOOD_TRUCK_CALENDAR_ID, 
		time_min=now, 
		time_max=now+timedelta(days=20), 
		single_events=True, 
		order_by='startTime',
	)
	return _create_events(raw_events)
	
def _create_events(raw_events):
	events = []
	for event in raw_events:
		events.append(Event(event))
	return events
