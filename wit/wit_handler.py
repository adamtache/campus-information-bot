# -*- coding: utf-8 -*-
from actions.actions import get_actions
from wit import Wit

WIT_ACCESS_TOKEN = "ZMFLGBX5RXBMZMW225EN2K43XTVTMUMV"

class WitHandler(object):

	def __init__(self):
		self.client = Wit(access_token=WIT_ACCESS_TOKEN, actions=get_actions())


	def handle(self, session_id, message):
		self.client.run_actions(session_id=session_id, message=message)
