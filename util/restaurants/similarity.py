# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

def get_closest_match(target, restaurants):
	sorted_by_similarity = get_restaurants_sorted_by_similarity(target, restaurants)
	return sorted_by_similarity[0] if len(sorted_by_similarity) != 0 else None

def get_restaurants_sorted_by_similarity(target, restaurants):
	return sorted(restaurants, key=lambda x: SequenceMatcher(None, x.name, target).ratio(), reverse=True)
