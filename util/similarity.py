# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

def get_closest_match(target, schedules):
	sorted_by_similarity = get_schedules_sorted_by_similarity_of_names(target, schedules)
	return sorted_by_similarity[0] if len(sorted_by_similarity) != 0 else None

def get_schedules_sorted_by_similarity_of_names(target, schedules):
	return sorted(schedules, key=lambda x: SequenceMatcher(None, x.name, target).ratio(), reverse=True)
