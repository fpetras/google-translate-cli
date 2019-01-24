#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from google.cloud import translate
from iso_639_1 import str_to_iso_639_1
from print_languages import decode, print_languages, print_language_name

if len(sys.argv) != 3:
	print('usage: ./translate.py "Text to translate" "Target language"')
	print_languages()
	sys.exit()

def translate_text(text, target_language):
	translate_client=translate.Client()
	result = translate_client.translate(text, target_language)

	print_language_name(result['detectedSourceLanguage'])
	print(result['input'])
	print_language_name(target_language)
	print(decode(result['translatedText']))

lang = str_to_iso_639_1(sys.argv[2])
translate_text(sys.argv[1], lang)
