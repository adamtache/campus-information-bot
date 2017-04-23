# -*- coding: utf-8 -*-
import webapp2

from cron_handlers import restaurant_handler
from google.appengine.ext.webapp.util import run_wsgi_app

class CronHandler(webapp2.RequestHandler):

	def get(self):
		restaurant_handler.scrape_and_add_to_db()

app = webapp2.WSGIApplication([
    (r'/cron', CronHandler),
], debug=True)

if __name__ == '__main__':
    run_wsgi_app(app)
