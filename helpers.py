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
  -h, --help  show this help message and exit
  -s          text-to-speech
  -f FILE     translate FILE
  -i          interactive mode''')

def valid_lang(lang):
	if lang == False:
		return False
	return True
