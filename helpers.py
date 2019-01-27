# -*- coding: utf-8 -*-

def credentials():
	print('''\
┌──────────────────────────────────────────────────────┐
│   You need a credentials file to use this version    │
│   Refer to README.md or instructions.txt             │
│   Or use the other version that doesn't need it      │
└──────────────────────────────────────────────────────┘''')
    	

def print_usage():
	print('''\
usage: ./translate.py [options] [Input to translate] [target language [...]]

optional arguments:
  -h, --help         show this help message and exit
  -c, --confidence   display detected language confidence level
  -s, --speech       activate text-to-speech
  -f, --file FILE    translate FILE
  -u, --url URL      translate web page (opens browser)
  -i, --interactive  interactive mode''')

def valid_lang(lang):
	if lang == False:
		return False
	return True
