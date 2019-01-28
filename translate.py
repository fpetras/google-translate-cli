#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from google.cloud import translate
from language_to_iso import lang_to_iso
from speech import text_to_speech
from web_page import web_page_translation
from print_languages import decode, print_languages, print_language_name
from helpers import credentials, print_usage, valid_lang

opt_s = None
opt_c = None

def translate_text(text, target_language):
	if len(text) > 10000:
		print ('Error: Text too large. Maximum: 10000 characters')
		sys.exit()
	try:
		client = translate.Client()
	except:
		credentials()
		sys.exit()
	try:
		confidence = client.detect_language(text)
		result = client.translate(text, target_language)
	except Exception as e:
		print('Error: '),
		print(e)
		sys.exit()
	if opt_c == True:
		print('Detected language confidence: '),
		print(confidence['confidence'])
	print_language_name(result['detectedSourceLanguage'])
	print(result['input'])
	print_language_name(target_language)
	print(decode(result['translatedText']))
	if opt_s == True:
		text_to_speech(result['translatedText'], target_language)

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
				lang = lang_to_iso(l, False, False)
				if valid_lang(lang) == True:
					translate_text(text, lang)
		f.close()

def interactive_translation():
	print ('Type CHANGE to change target language')
	print('Type EXIT to exit')
	try:
		lang = raw_input('Enter target language: ')
	except: # handles Ctrl-D / Ctrl-C
		print('')
		sys.exit()
	if lang == 'EXIT':
		sys.exit()
	lang = lang_to_iso(lang, True, False)
	text = ''
	try:
		while True:
			while valid_lang(lang) == False or text == 'CHANGE':
				text = ''
				lang = raw_input('Enter target language: ')
				if lang == 'EXIT':
					sys.exit()
				lang = lang_to_iso(lang, True, False)
				if valid_lang(lang) == True:
					print('✔︎')
			text = raw_input('Enter text to translate: ')
			if text == 'EXIT':
				sys.exit()
			if text == 'CHANGE':
				continue
			translate_text(text, lang)
	except: # handles Ctrl-D / Ctrl-C
		print('')
		sys.exit()

def main(argv):
	global opt_s
	global opt_c
	if '-s' in argv:
		opt_s = True
		argv.remove('-s')
	if '--speech' in argv:
		opt_s = True
		argv.remove('--speech')
	if '-c' in argv:
		opt_c = True
		argv.remove('-c')
	if '--confidence' in argv:
		opt_c = True
		argv.remove('--confidence')
	if len(argv) < 2 or argv[1] == '-h' or argv[1] == '--help':
		print_usage(1)
		print_languages(1)
		sys.exit()
	elif len(argv) >= 3 and (argv[1] == '-f' or argv[1] == '--file'):
		file_translation(argv)
	elif len(argv) >= 3 and (argv[1] == '-u' or argv[1] == '--url'):
		web_page_translation(argv)
	elif len(argv) >= 2 and (argv[1] == '-i' or argv[1] == '--interactive'):
		interactive_translation()
	elif len(argv) == 2:
		translate_text(argv[1], 'en')
	elif len(argv) > 2:
		for l in argv[2:]:
			lang = lang_to_iso(l, False, False)
			if valid_lang(lang) == True:
				translate_text(argv[1], lang)

if __name__ == "__main__":
	main(sys.argv)
