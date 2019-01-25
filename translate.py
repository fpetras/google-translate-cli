#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from google.cloud import translate
from iso_639_1 import str_to_iso_639_1
from print_languages import decode, print_languages, print_language_name

def translate_text(text, target_language):
	client = translate.Client()
	try:
		confidence = client.detect_language(text)
	except Exception as e:
		print ('Error: '),
		print e
		sys.exit()
	try:
		result = client.translate(text, target_language)
	except Exception as e:
		print('Error: '),
		print e
		sys.exit()
	print('Detected language confidence: '),
	print(confidence['confidence'])
	print_language_name(result['detectedSourceLanguage'])
	print(result['input'])
	print_language_name(target_language)
	print(decode(result['translatedText']))

def file_translation(argv):
	try:
		f = open(argv[2], 'r')
	except Exception:
		print("Error: Can't find file or read data")
		sys.exit()
	else:
		if f.mode == 'r':
			text = f.read(10000)
			if len(text) >= 10000:
				print ('Error: File too large. Maximum: 10000 characters')
				f.close()
				sys.exit()
		if len(argv) == 3: # if no language is given, default to English
			translate_text(text, 'en')
		else:
			for l in argv[3:]: # iterate through languages
				lang = str_to_iso_639_1(l)
				if lang != 404: # check if language is invalid
					translate_text(text, lang)
		f.close()

def interactive_translation():
	print('WIP')

def print_usage():
	print('''usage: translate.py [options] [Input to translate] [target language ...]

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     translate FILE
  -i          interactive mode''')

def main(argv):
	if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
		print_usage()
		print_languages()
		sys.exit()
	elif len(sys.argv) >= 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--file'):
		file_translation(sys.argv)
	elif len(sys.argv) >= 2 and (sys.argv[1] == '-i' or sys.argv[1] == '--interactive'):
		interactive_translation()
	elif len(sys.argv) == 2:
		translate_text(sys.argv[1], 'en')
	elif len(sys.argv) > 2:
		for l in sys.argv[2:]:
			lang = str_to_iso_639_1(l)
			if lang != 404: # check if language is invalid
				translate_text(sys.argv[1], lang)
#	if len(sys.argv) != 3:
#		print('usage: ./translate.py "Text to translate" "Target language"')
#		print_languages()
#		sys.exit()
#	lang = str_to_iso_639_1(sys.argv[2])
#	translate_text(sys.argv[1], lang)

if __name__ == "__main__":
	main(sys.argv)
