# -*- coding: utf-8 -*-
import sys

def print_languages():
	print('\nSupported languages:'),
	print('''
    ┌───────────────────────┬───────────────────────┬───────────────────────┐
    │ Afrikaans      - af   │ Hausa          - ha   │ Norwegian      - no   │
    │ Albanian       - sq   │ Hawaiian       - haw  │ Pashto         - ps   │
    │ Amharic        - am   │ Hebrew         - he   │ Persian        - fa   │
    │ Arabic         - ar   │ Hindi          - hi   │ Polish         - pl   │
    │ Armenian       - hy   │ Hmong          - hmv  │ Portuguese     - pt   │
    │ Azerbaijani    - az   │ Hungarian      - hu   │ Punjabi        - pa   │
    │ Basque         - eu   │ Icelandic      - is   │ Romanian       - ro   │
    │ Belarusian     - be   │ Igbo           - ig   │ Russian        - ru   │
    │ Bengali        - bn   │ Indonesian     - id   │ Samoan         - sm   │
    │ Bosnian        - bs   │ Irish          - ga   │ Scots Gaelic   - gd   │
    │ Bulgarian      - bg   │ Italian        - it   │ Serbian        - sr   │
    │ Catalan        - ca   │ Japanese       - ja   │ Sesotho        - st   │
    │ Cebuano        - ceb  │ Javanese       - jv   │ Shona          - sn   │
    │ Chichewa       - ny   │ Kannada        - kn   │ Sindhi         - sd   │
    │ Chinese        - zh   │ Kazakh         - kk   │ Sinhala        - si   │
    │ Chinese        - zh   │ Khmer          - km   │ Slovak         - sk   │
    │ Corsican       - co   │ Korean         - ko   │ Slovenian      - sl   │
    │ Croatian       - hr   │ Kurdish        - ku   │ Somali         - so   │
    │ Czech          - cs   │ Kyrgyz         - ky   │ Spanish        - es   │
    │ Danish         - da   │ Lao            - lo   │ Sundanese      - su   │
    │ Dutch          - nl   │ Latin          - la   │ Swahili        - sw   │
    │ English        - en   │ Latvian        - lv   │ Swedish        - sv   │
    │ Esperanto      - eo   │ Lithuanian     - lt   │ Tajik          - tg   │
    │ Estonian       - et   │ Luxembourgish  - lb   │ Tamil          - ta   │
    │ Filipino       - fil  │ Macedonian     - mk   │ Telugu         - te   │
    │ Finnish        - fi   │ Malagasy       - mg   │ Thai           - th   │
    │ French         - fr   │ Malay          - ms   │ Turkish        - tr   │
    │ Frisian        - fry  │ Malayalam      - ml   │ Ukrainian      - uk   │
    │ Galician       - gl   │ Maltese        - mt   │ Urdu           - ur   │
    │ Georgian       - ka   │ Maori          - mi   │ Uzbek          - uz   │
    │ German         - de   │ Marathi        - mr   │ Vietnamese     - vi   │
    │ Greek          - el   │ Mongolian      - mn   │ Welsh          - cy   │
    │ Gujarati       - gu   │ Myanmar        - my   │ Xhosa          - xh   │
    │ Haitian Creole - ht   │ Nepali         - ne   │ Yiddisg        - yi   │
    └───────────────────────┴───────────────────────┴───────────────────────┘''')

def str_to_iso_639_1(lang):
	if (lang.lower() == 'afrikaans' or lang.lower() == 'af'):
		return 'af'
	elif (lang.lower() == 'albanian' or lang.lower() == 'sq'):
		return 'sq'
	elif (lang.lower() == 'amharic' or lang.lower() == 'am'):
		return 'am'
	elif (lang.lower() == 'arabic' or lang.lower() == 'ar'):
		return 'ar'
	elif (lang.lower() == 'armenian' or lang.lower() == 'hy'):
		return 'hy'
	elif (lang.lower() == 'azerbaijani' or lang.lower() == 'az'):
		return 'az'
	elif (lang.lower() == 'basque' or lang.lower() == 'eu'):
		return 'eu'
	elif (lang.lower() == 'belarusian' or lang.lower() == 'be'):
		return 'be'
	elif (lang.lower() == 'bengali' or lang.lower() == 'bn'):
		return 'bn'
	elif (lang.lower() == 'bosnian' or lang.lower() == 'bs'):
		return 'bs'
	elif (lang.lower() == 'bulgarian' or lang.lower() == 'bg'):
		return 'bg'
	elif (lang.lower() == 'catalan' or lang.lower() == 'ca'):
		return 'ca'
	elif (lang.lower() == 'cebuano' or lang.lower() == 'ceb'):
		return 'ceb'
	elif (lang.lower() == 'chichewa' or lang.lower() == 'ny'):
		return 'ny'
	elif (lang.lower() == 'chinese' or lang.lower() == 'zh'):
		return 'zh'
	elif (lang.lower() == 'corsican' or lang.lower() == 'co'):
		return 'co'
	elif (lang.lower() == 'croatian' or lang.lower() == 'hr'):
		return 'hr'
	elif (lang.lower() == 'czech' or lang.lower() == 'cs'):
		return 'cs'
	elif (lang.lower() == 'danish' or lang.lower() == 'da'):
		return 'da'
	elif (lang.lower() == 'dutch' or lang.lower() == 'nl'):
		return 'nl'
	elif (lang.lower() == 'english' or lang.lower() == 'en'):
		return 'en'
	elif (lang.lower() == 'esperanto' or lang.lower() == 'eo'):
		return 'eo'
	elif (lang.lower() == 'estonian' or lang.lower() == 'et'):
		return 'et'
	elif (lang.lower() == 'filipino' or lang.lower() == 'fil'):
		return 'fil'
	elif (lang.lower() == 'finnish' or lang.lower() == 'fi'):
		return 'fi'
	elif (lang.lower() == 'french' or lang.lower() == 'fr'):
		return 'fr'
	elif (lang.lower() == 'frisian' or lang.lower() == 'fry'):
		return 'fry'
	elif (lang.lower() == 'galician' or lang.lower() == 'gl'):
		return ''
	elif (lang.lower() == 'georgian' or lang.lower() == 'ka'):
		return 'ka'
	elif (lang.lower() == 'german' or lang.lower() == 'de'):
		return 'de'
	elif (lang.lower() == 'greek' or lang.lower() == 'el'):
		return 'el'
	elif (lang.lower() == 'gujarati' or lang.lower() == 'gu'):
		return 'gu'
	elif (lang.lower() == 'haitian creole' or lang.lower() == 'ht'):
		return 'ht'
	elif (lang.lower() == 'hausa' or lang.lower() == 'ha'):
		return 'ha'
	elif (lang.lower() == 'hawaiian' or lang.lower() == 'haw'):
		return 'haw'
	elif (lang.lower() == 'hebrew' or lang.lower() == 'he'):
		return 'he'
	elif (lang.lower() == 'hindi' or lang.lower() == 'hi'):
		return 'hi'
	elif (lang.lower() == 'hmong' or lang.lower() == 'hmn'):
		return ''
	elif (lang.lower() == 'hungarian' or lang.lower() == 'hu'):
		return 'hu'
	elif (lang.lower() == 'icelandic' or lang.lower() == 'is'):
		return ''
	elif (lang.lower() == 'igbo' or lang.lower() == 'ig'):
		return 'ig'
	elif (lang.lower() == 'indonesian' or lang.lower() == 'id'):
		return 'id'
	elif (lang.lower() == 'irish' or lang.lower() == 'ga'):
		return 'ga'
	elif (lang.lower() == 'italian' or lang.lower() == 'it'):
		return 'it'
	elif (lang.lower() == 'japanese' or lang.lower() == 'ja'):
		return 'ja'
	elif (lang.lower() == 'kannada' or lang.lower() == 'kn'):
		return 'kn'
	elif (lang.lower() == 'kazakh' or lang.lower() == 'kk'):
		return 'kk'
	elif (lang.lower() == 'khmer' or lang.lower() == 'km'):
		return 'km'
	elif (lang.lower() == 'korean' or lang.lower() == 'ko'):
		return 'ko'
	elif (lang.lower() == 'kurdish' or lang.lower() == 'kurmanji' or
			lang.lower() == 'ku'):
		return ''
	elif (lang.lower() == 'kyrgyz' or lang.lower() == 'ky'):
		return 'ky'
	elif (lang.lower() == 'lao' or lang.lower() == 'lo'):
		return 'lo'
	elif (lang.lower() == 'latin' or lang.lower() == 'la'):
		return 'la'
	elif (lang.lower() == 'latvian' or lang.lower() == 'lv'):
		return 'lv'
	elif (lang.lower() == 'lithuanian' or lang.lower() == 'lt'):
		return 'lt'
	elif (lang.lower() == 'luxembourgish' or lang.lower() == 'lb'):
		return 'lb'
	elif (lang.lower() == 'macedonian' or lang.lower() == 'mk'):
		return 'mk'
	elif (lang.lower() == 'malagasy' or lang.lower() == 'mg'):
		return 'mg'
	elif (lang.lower() == 'malay' or lang.lower() == 'ms'):
		return 'ms'
	elif (lang.lower() == 'malayalam' or lang.lower() == 'ml'):
		return 'ml'
	elif (lang.lower() == 'maltese' or lang.lower() == 'mt'):
		return 'mt'
	elif (lang.lower() == 'maori' or lang.lower() == 'mi'):
		return 'mi'
	elif (lang.lower() == 'marathi' or lang.lower() == 'mr'):
		return 'mr'
	elif (lang.lower() == 'mongolian' or lang.lower() == 'mn'):
		return 'mn'
	elif (lang.lower() == 'myanmar' or lang.lower() == 'burmese' or
			lang.lower() == 'my'):
		return 'my'
	elif (lang.lower() == 'nepali' or lang.lower() == 'ne'):
		return 'ne'
	elif (lang.lower() == 'norwegian' or lang.lower() == 'no'):
		return 'no'
	elif (lang.lower() == 'pashto' or lang.lower() == 'ps'):
		return 'ps'
	elif (lang.lower() == 'persian' or lang.lower() == 'fa'):
		return 'fa'
	elif (lang.lower() == 'polish' or lang.lower() == 'pl'):
		return 'pl'
	elif (lang.lower() == 'portuguese' or lang.lower() == 'pt'):
		return 'pt'
	elif (lang.lower() == 'punjabi' or lang.lower() == 'pa'):
		return 'pa'
	elif (lang.lower() == 'romanian' or lang.lower() == 'ro'):
		return 'ro'
	elif (lang.lower() == 'russian' or lang.lower() == 'ru'):
		return 'ru'
	elif (lang.lower() == 'samoan' or lang.lower() == 'sm'):
		return 'sm'
	elif (lang.lower() == 'scots gaelic' or lang.lower() == 'gd'):
		return 'gd'
	elif (lang.lower() == 'serbian' or lang.lower() == 'sr'):
		return 'sr'
	elif (lang.lower() == 'sesotho' or lang.lower() == 'st'):
		return 'st'
	elif (lang.lower() == 'shona' or lang.lower() == 'sn'):
		return 'sn'
	elif (lang.lower() == 'sindhi' or lang.lower() == 'sd'):
		return 'sd'
	elif (lang.lower() == 'sinhala' or lang.lower() == 'si'):
		return 'si'
	elif (lang.lower() == 'slovak' or lang.lower() == 'sk'):
		return 'sk'
	elif (lang.lower() == 'slovenian' or lang.lower() == 'sl'):
		return 'sl'
	elif (lang.lower() == 'somali' or lang.lower() == 'so'):
		return 'so'
	elif (lang.lower() == 'spanish' or lang.lower() == 'es'):
		return 'es'
	elif (lang.lower() == 'sundanese' or lang.lower() == 'su'):
		return 'su'
	elif (lang.lower() == 'swahili' or lang.lower() == 'sw'):
		return 'sw'
	elif (lang.lower() == 'swedish' or lang.lower() == 'sv'):
		return 'sv'
	elif (lang.lower() == 'tajik' or lang.lower() == 'tg'):
		return 'tg'
	elif (lang.lower() == 'tamil' or lang.lower() == 'ta'):
		return 'ta'
	elif (lang.lower() == 'telugu' or lang.lower() == 'te'):
		return 'te'
	elif (lang.lower() == 'thai' or lang.lower() == 'th'):
		return 'th'
	elif (lang.lower() == 'turkish' or lang.lower() == 'tr'):
		return 'tr'
	elif (lang.lower() == 'ukrainian' or lang.lower() == 'uk'):
		return 'uk'
	elif (lang.lower() == 'urdu' or lang.lower() == 'ur'):
		return 'ur'
	elif (lang.lower() == 'uzbek' or lang.lower() == 'uz'):
		return 'uz'
	elif (lang.lower() == 'vietnamese' or lang.lower() == 'vi'):
		return 'vi'
	elif (lang.lower() == 'welsh' or lang.lower() == 'cy'):
		return 'cy'
	elif (lang.lower() == 'xhosa' or lang.lower() == 'xh'):
		return 'xh'
	elif (lang.lower() == 'yiddish' or lang.lower() == 'yi'):
		return 'yi'
	elif (lang.lower() == 'yoruba' or lang.lower() == 'yo'):
		return 'yo'
	elif (lang.lower() == 'zulu' or lang.lower() == 'zu'):
		return 'zu'
	else:
		print('Language not supported')
		sys.exit()
