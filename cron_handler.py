# -*- coding: utf-8 -*-
import webapp2

from datastore.handlers import schedules_handler
from util.scrapers.food_truck_scraper import FoodTruckScraper
from util.scrapers.restaurant_scraper import RestaurantScraper
from google.appengine.ext.webapp.util import run_wsgi_app

scrapers_to_use = [
	FoodTruckScraper(),
	RestaurantScraper(),
]

class CronHandler(webapp2.RequestHandler):

	def get(self):
		for scraper in scrapers_to_use:
			schedules_handler.scrape_and_put_in_db(scraper)

app = webapp2.WSGIApplication([
    (r'/cron', CronHandler),
], debug=True)

if __name__ == '__main__':
    run_wsgi_app(app)
