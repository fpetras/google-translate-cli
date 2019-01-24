# -*- coding: utf-8 -*-

import HTMLParser

def decode(string):
	decode = HTMLParser.HTMLParser()
	return decode.unescape(string)

def print_languages():
	print('\nSupported languages:'),
	print('''
    ┌───────────────────────┬───────────────────────┬───────────────────────┐
    │ Afrikaans      - af   │ Hebrew         - he   │ Polish         - pl   │
    │ Albanian       - sq   │ Hindi          - hi   │ Portuguese     - pt   │
    │ Amharic        - am   │ Hmong          - hmv  │ Punjabi        - pa   │
    │ Arabic         - ar   │ Hungarian      - hu   │ Romanian       - ro   │
    │ Armenian       - hy   │ Icelandic      - is   │ Russian        - ru   │
    │ Azerbaijani    - az   │ Igbo           - ig   │ Samoan         - sm   │
    │ Basque         - eu   │ Indonesian     - id   │ Scots Gaelic   - gd   │
    │ Belarusian     - be   │ Irish          - ga   │ Serbian        - sr   │
    │ Bengali        - bn   │ Italian        - it   │ Sesotho        - st   │
    │ Bosnian        - bs   │ Japanese       - ja   │ Shona          - sn   │
    │ Bulgarian      - bg   │ Javanese       - jv   │ Sindhi         - sd   │
    │ Catalan        - ca   │ Kannada        - kn   │ Sinhala        - si   │
    │ Cebuano        - ceb  │ Kazakh         - kk   │ Slovak         - sk   │
    │ Chichewa       - ny   │ Khmer          - km   │ Slovenian      - sl   │
    │ Chinese        - zh   │ Korean         - ko   │ Somali         - so   │
    │ Corsican       - co   │ Kurdish        - ku   │ Spanish        - es   │
    │ Croatian       - hr   │ Kyrgyz         - ky   │ Sundanese      - su   │
    │ Czech          - cs   │ Lao            - lo   │ Swahili        - sw   │
    │ Danish         - da   │ Latin          - la   │ Swedish        - sv   │
    │ Dutch          - nl   │ Latvian        - lv   │ Tajik          - tg   │
    │ English        - en   │ Lithuanian     - lt   │ Tamil          - ta   │
    │ Esperanto      - eo   │ Luxembourgish  - lb   │ Telugu         - te   │
    │ Estonian       - et   │ Macedonian     - mk   │ Thai           - th   │
    │ Filipino       - fil  │ Malagasy       - mg   │ Turkish        - tr   │
    │ Finnish        - fi   │ Malay          - ms   │ Ukrainian      - uk   │
    │ French         - fr   │ Malayalam      - ml   │ Urdu           - ur   │
    │ Frisian        - fry  │ Maltese        - mt   │ Uzbek          - uz   │
    │ Galician       - gl   │ Maori          - mi   │ Vietnamese     - vi   │
    │ Georgian       - ka   │ Marathi        - mr   │ Welsh          - cy   │
    │ German         - de   │ Mongolian      - mn   │ Xhosa          - xh   │
    │ Greek          - el   │ Myanmar        - my   │ Yiddish        - yi   │
    │ Gujarati       - gu   │ Nepali         - ne   │ Yoruba         - yo   │
    │ Haitian Creole - ht   │ Norwegian      - no   │ Zulu           - zu   │
    │ Hausa          - ha   │ Pashto         - ps   │                       │
    │ Hawaiian       - haw  │ Persian        - fa   │                       │
    └───────────────────────┴───────────────────────┴───────────────────────┘''')

def print_language_name(lang):
	if (lang.lower() == 'afrikaans' or lang.lower() == 'af' or lang.lower() == 'afr'):
		print 'Afrikaans: ',
	elif (lang.lower() == 'albanian' or lang.lower() == 'sq' or lang.lower() == 'sqi' or lang.lower() == 'alb'):
		print 'Albanian: ',
	elif (lang.lower() == 'amharic' or lang.lower() == 'am' or lang.lower() == 'amh'):
		print 'Amharic: ',
	elif (lang.lower() == 'arabic' or lang.lower() == 'ar' or lang.lower() == 'ara'):
		print 'Arabic: ',
	elif (lang.lower() == 'armenian' or lang.lower() == 'hy' or lang.lower() == 'arm' or lang.lower() == 'hye'):
		print 'Armenian: ',
	elif (lang.lower() == 'azerbaijani' or lang.lower() == 'az' or lang.lower() == 'aze'):
		print 'Azerbaijani: ',
	elif (lang.lower() == 'basque' or lang.lower() == 'eu' or lang.lower() == 'eur' or lang.lower() == 'baq'):
		print 'Basque: ',
	elif (lang.lower() == 'belarusian' or lang.lower() == 'be' or lang.lower() == 'bel'):
		print 'Belarusian: ',
	elif (lang.lower() == 'bengali' or lang.lower() == 'bn' or lang.lower() == 'ben'):
		print 'Bengali:'
	elif (lang.lower() == 'bosnian' or lang.lower() == 'bs' or lang.lower() == 'bos'):
		print 'Bosnian: ',
	elif (lang.lower() == 'bulgarian' or lang.lower() == 'bg' or lang.lower() == 'bul'):
		print 'Bulgarian: ',
	elif (lang.lower() == 'catalan' or lang.lower() == 'ca' or lang.lower() == 'cat'):
		print 'Catalan: ',
	elif (lang.lower() == 'cebuano' or lang.lower() == 'ceb'):
		print 'Cebuano: ',
	elif (lang.lower() == 'chichewa' or lang.lower() == 'ny' or lang.lower() == 'nya'):
		print 'Chichewa: ',
	elif (lang.lower() == 'chinese' or lang.lower() == 'zh' or lang.lower() == 'zho' or lang.lower() == 'chi'):
		print 'Chinese: ',
	elif (lang.lower() == 'corsican' or lang.lower() == 'co' or lang.lower() == 'cos'):
		print 'Corsican: ',
	elif (lang.lower() == 'croatian' or lang.lower() == 'hr' or lang.lower() == 'hrw'):
		print 'Croatian: ',
	elif (lang.lower() == 'czech' or lang.lower() == 'cs' or lang.lower() == 'ces' or lang.lower() == 'cze'):
		print 'Czech: ',
	elif (lang.lower() == 'danish' or lang.lower() == 'da' or lang.lower() == 'dan'):
		print 'Danish: ',
	elif (lang.lower() == 'dutch' or lang.lower() == 'nl' or lang.lower() == 'nld' or lang.lower() == 'dut'):
		print 'Dutch: ',
	elif (lang.lower() == 'english' or lang.lower() == 'en' or lang.lower() == 'eng'):
		print 'English: ',
	elif (lang.lower() == 'esperanto' or lang.lower() == 'eo' or lang.lower() == 'epo'):
		print 'Esperanto: ',
	elif (lang.lower() == 'estonian' or lang.lower() == 'et' or lang.lower() == 'est'):
		print 'Estonian: ',
	elif (lang.lower() == 'filipino' or lang.lower() == 'fil'):
		print 'Filipino: ',
	elif (lang.lower() == 'finnish' or lang.lower() == 'fi' or lang.lower() == 'fin'):
		print 'Finnish: ',
	elif (lang.lower() == 'french' or lang.lower() == 'fr' or lang.lower() == 'fre' or lang.lower() == 'fra'):
		print 'French: ',
	elif (lang.lower() == 'frisian' or lang.lower() == 'fry' or lang.lower() == 'frr' or lang.lower() == 'frs'):
		print 'Frisian: ',
	elif (lang.lower() == 'galician' or lang.lower() == 'gl' or lang.lower() == 'glg'):
		print 'Galician: ',
	elif (lang.lower() == 'georgian' or lang.lower() == 'ka' or lang.lower() == 'kat' or lang.lower() == 'geo'):
		print 'Georgian: ',
	elif (lang.lower() == 'german' or lang.lower() == 'de' or lang.lower() == 'deu' or lang.lower() == 'ger'):
		print 'German: ',
	elif (lang.lower() == 'greek' or lang.lower() == 'el' or lang.lower() == 'ell' or lang.lower() == 'gre'):
		print 'Greek: ',
	elif (lang.lower() == 'gujarati' or lang.lower() == 'gu' or lang.lower() == 'guj'):
		print 'Gujarati: ',
	elif (lang.lower() == 'haitian creole' or lang.lower() == 'haitian' or lang.lower() == 'ht' or lang.lower() == 'hat'):
		print 'Haitian Creole: ',
	elif (lang.lower() == 'hausa' or lang.lower() == 'ha' or lang.lower() == 'hau'):
		print 'Hausa: ',
	elif (lang.lower() == 'hawaiian' or lang.lower() == 'haw'):
		print 'Hawaiian: ',
	elif (lang.lower() == 'hebrew' or lang.lower() == 'he' or lang.lower() == 'heb'):
		print 'Hebrew: ',
	elif (lang.lower() == 'hindi' or lang.lower() == 'hi' or lang.lower() == 'hin'):
		print 'Hindi: ',
	elif (lang.lower() == 'hmong' or lang.lower() == 'hmn'):
		print 'Hmong: ',
	elif (lang.lower() == 'hungarian' or lang.lower() == 'hu' or lang.lower() == 'hun'):
		print 'Hungarian: ',
	elif (lang.lower() == 'icelandic' or lang.lower() == 'is' or lang.lower() == 'isl' or lang.lower() == 'ice'):
		print 'Icelandic: ',
	elif (lang.lower() == 'igbo' or lang.lower() == 'ig' or lang.lower() == 'ibo'):
		print 'Igbo: ',
	elif (lang.lower() == 'indonesian' or lang.lower() == 'id' or lang.lower() == 'ind'):
		print 'Indonesian: ',
	elif (lang.lower() == 'irish' or lang.lower() == 'ga' or lang.lower() == 'gle'):
		print 'Irish: ',
	elif (lang.lower() == 'italian' or lang.lower() == 'it' or lang.lower() == 'ita'):
		print 'Italian: ',
	elif (lang.lower() == 'japanese' or lang.lower() == 'ja' or lang.lower() == 'jpn'):
		print 'Japanese: ',
	elif (lang.lower() == 'javanese' or lang.lower() == 'jv' or lang.lower() == 'jav'):
		print 'Javanese: ',
	elif (lang.lower() == 'kannada' or lang.lower() == 'kn' or lang.lower() == 'kan'):
		print 'Kannada: ',
	elif (lang.lower() == 'kazakh' or lang.lower() == 'kk' or lang.lower() == 'kaz'):
		print 'Kazakh: ',
	elif (lang.lower() == 'khmer' or lang.lower() == 'km' or lang.lower() == 'khm'):
		print 'Khmer: ',
	elif (lang.lower() == 'korean' or lang.lower() == 'ko' or lang.lower() == 'kor'):
		print 'Korean: ',
	elif (lang.lower() == 'kurdish' or lang.lower() == 'kurmanji' or lang.lower() == 'ku' or lang.lower() == 'kur'):
		print 'Kurdish: ',
	elif (lang.lower() == 'kyrgyz' or lang.lower() == 'ky' or lang.lower() == 'kir'):
		print 'Kyrgyz: ',
	elif (lang.lower() == 'lao' or lang.lower() == 'lo'):
		print 'Lao: ',
	elif (lang.lower() == 'latin' or lang.lower() == 'la' or lang.lower() == 'lat'):
		print 'Latin: ',
	elif (lang.lower() == 'latvian' or lang.lower() == 'lv' or lang.lower() == 'lav'):
		print 'Latvian: ',
	elif (lang.lower() == 'lithuanian' or lang.lower() == 'lt' or lang.lower() == 'lit'):
		print 'Lithuanian: ',
	elif (lang.lower() == 'luxembourgish' or lang.lower() == 'lb' or lang.lower() == 'ltz'):
		print 'Luxembourgish: ',
	elif (lang.lower() == 'macedonian' or lang.lower() == 'mk' or lang.lower() == 'mkd' or lang.lower() == 'mac'):
		print 'Macedonian: ',
	elif (lang.lower() == 'malagasy' or lang.lower() == 'mg' or lang.lower() == 'mlg'):
		print 'Malagasy: ',
	elif (lang.lower() == 'malay' or lang.lower() == 'ms' or lang.lower() == 'msa' or lang.lower() == 'may'):
		print 'Malay: ',
	elif (lang.lower() == 'malayalam' or lang.lower() == 'ml' or lang.lower() == 'mal'):
		print 'Malayalam: ',
	elif (lang.lower() == 'maltese' or lang.lower() == 'mt' or lang.lower() == 'mlt'):
		print 'Maltese: ',
	elif (lang.lower() == 'maori' or lang.lower() == 'mi' or lang.lower() == 'mao' or lang.lower() == 'mri'):
		print 'Maori: ',
	elif (lang.lower() == 'marathi' or lang.lower() == 'mr' or lang.lower() == 'mar'):
		print 'Marathi: ',
	elif (lang.lower() == 'mongolian' or lang.lower() == 'mn' or lang.lower() == 'mon'):
		print 'Mongolian: ',
	elif (lang.lower() == 'myanmar' or lang.lower() == 'burmese' or lang.lower() == 'my' or lang.lower() == 'mya' or lang.lower() == 'bur'):
		print 'Myanmar: ',
	elif (lang.lower() == 'nepali' or lang.lower() == 'ne' or lang.lower() == 'nep'):
		print 'Nepali: ',
	elif (lang.lower() == 'norwegian' or lang.lower() == 'no' or lang.lower() == 'nor'):
		print 'Norwegian: ',
	elif (lang.lower() == 'pashto' or lang.lower() == 'ps' or lang.lower() == 'pus'):
		print 'Pashto: ',
	elif (lang.lower() == 'persian' or lang.lower() == 'fa' or lang.lower() == 'fas' or lang.lower() == 'per'):
		print 'Persian: ',
	elif (lang.lower() == 'polish' or lang.lower() == 'pl' or lang.lower() == 'pol'):
		print 'Polish: ',
	elif (lang.lower() == 'portuguese' or lang.lower() == 'pt' or lang.lower() == 'por'):
		print 'Portuguese: ',
	elif (lang.lower() == 'punjabi' or lang.lower() == 'pa' or lang.lower() == 'pan'):
		print 'Punjabi: ',
	elif (lang.lower() == 'romanian' or lang.lower() == 'ro' or lang.lower() == 'ron' or lang.lower() == 'rum'):
		print 'Romanian: ',
	elif (lang.lower() == 'russian' or lang.lower() == 'ru' or lang.lower() == 'rus'):
		print 'Russian: ',
	elif (lang.lower() == 'samoan' or lang.lower() == 'sm' or lang.lower() == 'smo'):
		print 'Samoan: ',
	elif (lang.lower() == 'scots gaelic' or lang.lower() == 'scottish gaelic' or lang.lower() == 'gaelic' or lang.lower() == 'gd' or lang.lower() == 'gla'):
		print 'Scots Gaelic: ',
	elif (lang.lower() == 'serbian' or lang.lower() == 'sr' or lang.lower() == 'srp'):
		print 'Serbian: ',
	elif (lang.lower() == 'sesotho' or lang.lower() == 'sotho' or lang.lower() == 'st' or lang.lower() == 'sot'):
		print 'Sesotho: ',
	elif (lang.lower() == 'shona' or lang.lower() == 'sn' or lang.lower() == 'sna'):
		print 'Shona: ',
	elif (lang.lower() == 'sindhi' or lang.lower() == 'sd' or lang.lower() == 'snd'):
		print 'Sindhi: ',
	elif (lang.lower() == 'sinhala' or lang.lower() == 'si' or lang.lower() == 'sin'):
		print 'Sinhala: ',
	elif (lang.lower() == 'slovak' or lang.lower() == 'sk' or lang.lower() == 'slk' or lang.lower() == 'slo'):
		print 'Slovak: ',
	elif (lang.lower() == 'slovenian' or lang.lower() == 'sl' or lang.lower() == 'slv'):
		print 'Slovenian: ',
	elif (lang.lower() == 'somali' or lang.lower() == 'so' or lang.lower() == 'som'):
		print 'Somali: ',
	elif (lang.lower() == 'spanish' or lang.lower() == 'es' or lang.lower() == 'spa'):
		print 'Spanish: ',
	elif (lang.lower() == 'sundanese' or lang.lower() == 'su' or lang.lower() == 'sun'):
		print 'Sudanese: ',
	elif (lang.lower() == 'swahili' or lang.lower() == 'sw' or lang.lower() == 'swa'):
		print 'Swahili: ',
	elif (lang.lower() == 'swedish' or lang.lower() == 'sv' or lang.lower() == 'swe'):
		print 'Swedish: ',
	elif (lang.lower() == 'tajik' or lang.lower() == 'tg' or lang.lower() == 'tgk'):
		print 'Tajik: ',
	elif (lang.lower() == 'tamil' or lang.lower() == 'ta' or lang.lower() == 'tam'):
		print 'Tamil: ',
	elif (lang.lower() == 'telugu' or lang.lower() == 'te' or lang.lower() == 'tel'):
		print 'Telugu: ',
	elif (lang.lower() == 'thai' or lang.lower() == 'th' or lang.lower() == 'tha'):
		print 'Thai: ',
	elif (lang.lower() == 'turkish' or lang.lower() == 'tr' or lang.lower() == 'tur'):
		print 'Turkish: ',
	elif (lang.lower() == 'ukrainian' or lang.lower() == 'uk' or lang.lower() == 'ukr'):
		print 'Ukrainian: ',
	elif (lang.lower() == 'urdu' or lang.lower() == 'ur' or lang.lower() == 'urd'):
		print 'Urdu: ',
	elif (lang.lower() == 'uzbek' or lang.lower() == 'uz' or lang.lower() == 'uzb'):
		print 'Uzbek: ',
	elif (lang.lower() == 'vietnamese' or lang.lower() == 'vi' or lang.lower() == 'vie'):
		print 'Vietnamese: ',
	elif (lang.lower() == 'welsh' or lang.lower() == 'cy' or lang.lower() == 'cym' or lang.lower() == 'wel'):
		print 'Welsh: ',
	elif (lang.lower() == 'xhosa' or lang.lower() == 'xh' or lang.lower() == 'xho'):
		print 'Xhosa: ',
	elif (lang.lower() == 'yiddish' or lang.lower() == 'yi' or lang.lower() == 'yid'):
		print 'Yiddish: ',
	elif (lang.lower() == 'yoruba' or lang.lower() == 'yo' or lang.lower() == 'yor'):
		print 'Yoruba: ',
	elif (lang.lower() == 'zulu' or lang.lower() == 'zu' or lang.lower() == 'zul'):
		print 'Zulu: ',
