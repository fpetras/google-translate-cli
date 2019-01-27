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
		return False
	if lang_to_iso(corrected, False, True) != False:
		print("Did you mean '" + corrected.capitalize() + "'?")
		return corrected
	return False

# Returns iso_639_1 code, checks spelling

def lang_to_iso(lang, interactive, spell_check):
	iso = languages(lang)
	if iso != False:
		return iso
	else:
		if spell_check == True:
			return False
		if interactive == False:
			print("'" + lang + "' is not a valid language")
		else:
			print('✘')
		try:
			with time_limit(2):
				if lang.isalnum() == True:
					corrected = check_spelling(lang.lower())
					if corrected != False:
						return languages(corrected)
		except TimeoutException:
			pass
		return False


