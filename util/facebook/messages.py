# -*- coding: utf-8 -*-
class Attachment(object):

	def __init__(self, attachment_type, payload):
		self.attachment_type = attachment_type
		self.payload = payload

	def get_audio(self):
		if self.attachment_type is 'audio':
			return self._get_url_from_payload()
		return ''

	def get_image(self):
		if self.attachment_type is 'image':
			return self._get_url_from_payload()
		return ''

	def get_video(self):
		if self.attachment_type is 'video':
			return self._get_url_from_payload()
		return ''

	def get_file(self):
		if self.attachment_type is 'file':
			return self._get_url_from_payload()
		return ''

	def _get_url_from_payload(self):
		if self.payload is None:
			return ''
		return self.payload.get('url')

	def get_location(self):
		if self.attachment_type is 'location':
			if self.payload is None:
				return ''
			coordinates = payload.get('coordinates')
			if coordinates is None:
				return ''
			return coordinates['lat'], coordinates['long']
		return ''
