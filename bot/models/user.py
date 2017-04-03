import json

class User(object):

	def __init__(self, user_json):
		data = json.loads(user_json)
		self.first_name = data['first_name']
		self.last_name = data['last_name']
		self.locale = data['locale']
		self.timezone = data['timezone']
