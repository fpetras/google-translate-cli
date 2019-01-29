# -*- coding: utf-8 -*-

def credentials():
	print('''\
┌──────────────────────────────────────────────────────┐
│   You need a credentials file to use this version    │
│   Refer to README.md or instructions.txt             │
│   Or use the other version that doesn't need it      │
└──────────────────────────────────────────────────────┘''')
    	
def print_usage(version, name):
	if version == 1:
		print('''\
usage: ''' + name + ''' [options] [Input to translate] [target language [...]]

\033[1;37moptional arguments:\033[0;0m
  -h, --help         show this help message and exit
  -l, --languages    print supported languages and exit
  -b, --bare         output the bare translation
  -c, --confidence   display detected language confidence level
  -s, --speech       activate text-to-speech
  -f, --file FILE    translate FILE
  -u, --url URL      translate web page (opens browser)
  -i, --interactive  interactive mode''')
	elif version == 2:
		print('''\
usage: ''' + name + ''' [options] [Input to translate] [target language [...]]

\033[1;37moptional arguments:\033[0;0m
  -h, --help         show this help message and exit
  -l, --languages    print supported languages and exit
  -b, --bare         output the bare translation
  -c, --confidence   display detected language confidence level
  -f, --file FILE    translate FILE
  -u, --url URL      translate web page (opens browser)
  -i, --interactive  interactive mode''')

def valid_lang(lang):
	if lang == False:
		return False
	return True
