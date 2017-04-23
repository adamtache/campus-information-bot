# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

def get_strings_sorted_by_similarity(str_comp, strings):
	return sorted(strings, key=lambda x: SequenceMatcher(None, x, str_comp).ratio(), reverse=True)

def get_closest_match(target, options):
	sorted_by_similarity = get_strings_sorted_by_similarity(target, options)
	return sorted_by_similarity[0] if len(sorted_by_similarity) != 0 else None
