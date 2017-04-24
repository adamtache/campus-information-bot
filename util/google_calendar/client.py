# -*- coding: utf-8 -*-
# Code modified from Google, licensed under the Apache License, Version 2.0
import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_events_from_calendar(calendar_id, time_min, time_max, single_events, order_by):
	eventsResult = _get_service().events().list(
		calendarId=calendar_id, 
		timeMin=time_min, 
		timeMax=time_max,
		singleEvents=single_events, 
		orderBy=order_by,
	).execute()
	return eventsResult.get('items', [])

def _get_service():
	scopes = [
		'https://www.googleapis.com/auth/calendar',
		'https://www.googleapis.com/auth/calendar.readonly',
	]
	credentials = ServiceAccountCredentials.from_json_keyfile_name(
		'campus-information-bot-71176d582072.json', 
		scopes=scopes,
	)
	http = credentials.authorize(httplib2.Http())
	return build('calendar', 'v3', http=http)
