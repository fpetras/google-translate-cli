import os
import sys
import urllib2
from timeout import *
from language_to_iso import lang_to_iso
from helpers import valid_lang

TRANSLATE_URL = 'https://translate.google.com/translate?sl=auto&tl='
TRANSLATE_URL_EN = 'https://translate.google.com/translate?sl=auto&tl=en&u='

def web_page_translation(argv):
	url = argv[2]
	if url.startswith('http://') == False and url.startswith('https://') == False:
		url = 'https://' + url
	try:
		with time_limit(5):
			urllib2.urlopen(url)
	except KeyboardInterrupt:
		print('')
		sys.exit()
	except TimeoutException:
		print('Error: Timeout')
		sys.exit()
	except:
		print('Error: Web site could not be reached')
		sys.exit()
	if len(argv) > 3:
		lang = lang_to_iso(argv[3], False, False)
		if valid_lang(lang) == False:
			sys.exit()
		url = TRANSLATE_URL + lang + '&u=' + url
	else:
		url = TRANSLATE_URL_EN + url
	try:
		os.system("open '" + url + "'")
	except:
		print('Error: URL could not be opened')
