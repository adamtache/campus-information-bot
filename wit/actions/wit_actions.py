# -*- coding: utf-8 -*-
def sanitize_input(input):
	return re.sub('\s+', '', input).lower()

def get_context_and_entities(request):
	return request['context'], request['entities']

def get_first_entity_value(entities, entity):
	if entity not in entities:
		return None
	value = entities[entity][0]['value']
	if not value:
		return None
	return value['value'] if isinstance(val, dict) else val
