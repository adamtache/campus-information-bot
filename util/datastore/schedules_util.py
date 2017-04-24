# -*- coding: utf-8 -*-
from datastore.models.schedule import Schedule

def get_schedule(schedule_name):
	return Schedule.query(Schedule.name == schedule_name)

def get_all_schedules():
	q = Schedule.query().order(-Schedule.name)
	schedules = []
	for schedule in q:
		schedules.append(schedule)
	return schedules
