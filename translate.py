#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.cloud import translate
import sys
from user_friendly import str_to_iso_639_1
from user_friendly import print_languages

if len(sys.argv) != 3:
	print('usage: ./translate.py "Text to translate" "Target language"')
	print_languages()
	sys.exit()

def translate_text(text, target_language):
	translate_client=translate.Client()
	result = translate_client.translate(text, target_language)

	print(result['input'])
	print('Detected source language: ' + result['detectedSourceLanguage'])
	print(result['translatedText'])

lang = str_to_iso_639_1(sys.argv[2])
translate_text(sys.argv[1], lang)
