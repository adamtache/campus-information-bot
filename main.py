# -*- coding: utf-8 -*-
import bot
import requests

from datastore import config
from requests_toolbelt.adapters import appengine

# Use AppEngineAdapter to support GAE with requests
appengine.monkeypatch()
app = bot.create_app(config)

if __name__ == '__main__':
	app.run(debug=True)
