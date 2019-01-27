# -*- coding: utf-8 -*-

from languages import languages
from timeout import *
try:
	from spellchecker import SpellChecker
except:
	pass

def check_spelling(lang):
	try:
		spell = SpellChecker()
		corrected = spell.correction(lang)
	except:
		return
	if lang_to_iso(corrected, False, True) != False:
		print("Did you mean '" + corrected.capitalize() + "'?")

# Returns iso_639_1 code, checks spelling in interactive mode

def lang_to_iso(lang, interactive, spell_check):
	iso = languages(lang)
	if iso != False:
		return iso
	else:
		if spell_check == True:
			return False
		if interactive == False:
			print('Language not supported')
		else:
			print('✘')
		try:
			with time_limit(2):
				if lang.isalnum() == True:
					check_spelling(lang.lower())
		except TimeoutException:
			pass
		return False


