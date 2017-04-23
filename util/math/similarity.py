# -*- coding: utf-8 -*-
import re

from difflib import SequenceMatcher

def get_strings_sorted_by_similarity(str_comp, strings):
	return sorted(strings, key=lambda x: SequenceMatcher(None, x, str_comp).ratio(), reverse=True)

def get_closest_match(target, options):
	sorted_by_similarity = get_strings_sorted_by_similarity(target, options)
	return sorted_by_similarity[0] if len(sorted_by_similarity) != 0 else None

def get_similarity_ratio(str1, str2):
	return SequenceMatcher(None, str1, str2).ratio()

def any_word_meets_threshold(string, target, threshold):
	words_in_string = re.split('\s+', string)
	for word in words_in_string:
		if meets_threshold(word, target, threshold):
			return True
	return False

def meets_threshold(word, target, threshold):
	return get_similarity_ratio(word, target) >= threshold
