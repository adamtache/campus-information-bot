# -*- coding: utf-8 -*-
from datastore.models.availability import Availability
from datastore.models.schedule import Schedule
from google.appengine.ext import ndb
from util.constants.schedules import DEFAULT_SCHEDULES_NAME

def scrape_and_put_in_db(scraper):
	for schedule in scraper.get_schedules():
		_put_schedule_in_db(schedule)

def _put_schedule_in_db(schedule):
	parent = _get_schedule_key(DEFAULT_SCHEDULES_NAME)
	name = schedule.name
	availabilities = _get_datastore_availabilities(
		schedule.availabilities,
	)
	Schedule(parent=parent, name=name, availabilities=availabilities).put()

def _get_schedule_key(schedules_name):
	"""Constructs a Datastore key for Schedules entity.

	Uses schedules_name as the key.
	"""
	return ndb.Key('Schedules', schedules_name)

def _get_datastore_availabilities(availabilities):
	datastore_availabilities = []
	for availability in availabilities:
		datastore_availabilities.append(_get_availability_for_datastore(availability))
	return datastore_availabilities

def _get_availability_for_datastore(availability):
	location = availability.location
	opens_at = availability.opens_at
	closes_at = availability.closes_at
	return Availability(
		date=availability.date,
		opens_at=opens_at.replace(tzinfo=None) if opens_at is not None else None,
		closes_at=closes_at.replace(tzinfo=None) if closes_at is not None else None,
		location=location if location is not None else '',
	)
