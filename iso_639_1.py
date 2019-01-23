import sys

def str_to_iso_639_1(lang):
	if (lang.lower() == 'afrikaans' or lang.lower() == 'af' or lang.lower() == 'afr'):
		return 'af'
	elif (lang.lower() == 'albanian' or lang.lower() == 'sq' or lang.lower() == 'sqi' or lang.lower() == 'alb'):
		return 'sq'
	elif (lang.lower() == 'amharic' or lang.lower() == 'am' or lang.lower() == 'amh'):
		return 'am'
	elif (lang.lower() == 'arabic' or lang.lower() == 'ar' or lang.lower() == 'ara'):
		return 'ar'
	elif (lang.lower() == 'armenian' or lang.lower() == 'hy' or lang.lower() == 'arm' or lang.lower() == 'hye'):
		return 'hy'
	elif (lang.lower() == 'azerbaijani' or lang.lower() == 'az' or lang.lower() == 'aze'):
		return 'az'
	elif (lang.lower() == 'basque' or lang.lower() == 'eu' or lang.lower() == 'eur' or lang.lower() == 'baq'):
		return 'eu'
	elif (lang.lower() == 'belarusian' or lang.lower() == 'be' or lang.lower() == 'bel'):
		return 'be'
	elif (lang.lower() == 'bengali' or lang.lower() == 'bn' or lang.lower() == 'ben'):
		return 'bn'
	elif (lang.lower() == 'bosnian' or lang.lower() == 'bs' or lang.lower() == 'bos'):
		return 'bs'
	elif (lang.lower() == 'bulgarian' or lang.lower() == 'bg' or lang.lower() == 'bul'):
		return 'bg'
	elif (lang.lower() == 'catalan' or lang.lower() == 'ca' or lang.lower() == 'cat'):
		return 'ca'
	elif (lang.lower() == 'cebuano' or lang.lower() == 'ceb'):
		return 'ceb'
	elif (lang.lower() == 'chichewa' or lang.lower() == 'ny' or lang.lower() == 'nya'):
		return 'ny'
	elif (lang.lower() == 'chinese' or lang.lower() == 'zh' or lang.lower() == 'zho' or lang.lower() == 'chi'):
		return 'zh'
	elif (lang.lower() == 'corsican' or lang.lower() == 'co' or lang.lower() == 'cos'):
		return 'co'
	elif (lang.lower() == 'croatian' or lang.lower() == 'hr' or lang.lower() == 'hrw'):
		return 'hr'
	elif (lang.lower() == 'czech' or lang.lower() == 'cs' or lang.lower() == 'ces' or lang.lower() == 'cze'):
		return 'cs'
	elif (lang.lower() == 'danish' or lang.lower() == 'da' or lang.lower() == 'dan'):
		return 'da'
	elif (lang.lower() == 'dutch' or lang.lower() == 'nl' or lang.lower() == 'nld' or lang.lower() == 'dut'):
		return 'nl'
	elif (lang.lower() == 'english' or lang.lower() == 'en' or lang.lower() == 'eng'):
		return 'en'
	elif (lang.lower() == 'esperanto' or lang.lower() == 'eo' or lang.lower() == 'epo'):
		return 'eo'
	elif (lang.lower() == 'estonian' or lang.lower() == 'et' or lang.lower() == 'est'):
		return 'et'
	elif (lang.lower() == 'filipino' or lang.lower() == 'fil'):
		return 'fil'
	elif (lang.lower() == 'finnish' or lang.lower() == 'fi' or lang.lower() == 'fin'):
		return 'fi'
	elif (lang.lower() == 'french' or lang.lower() == 'fr' or lang.lower() == 'fre' or lang.lower() == 'fra'):
		return 'fr'
	elif (lang.lower() == 'frisian' or lang.lower() == 'fry' or lang.lower() == 'frr' or lang.lower() == 'frs'):
		return 'fry'
	elif (lang.lower() == 'galician' or lang.lower() == 'gl' or lang.lower() == 'glg'):
		return 'gl'
	elif (lang.lower() == 'georgian' or lang.lower() == 'ka' or lang.lower() == 'kat' or lang.lower() == 'geo'):
		return 'ka'
	elif (lang.lower() == 'german' or lang.lower() == 'de' or lang.lower() == 'deu' or lang.lower() == 'ger'):
		return 'de'
	elif (lang.lower() == 'greek' or lang.lower() == 'el' or lang.lower() == 'ell' or lang.lower() == 'gre'):
		return 'el'
	elif (lang.lower() == 'gujarati' or lang.lower() == 'gu' or lang.lower() == 'guj'):
		return 'gu'
	elif (lang.lower() == 'haitian creole' or lang.lower() == 'haitian' or lang.lower() == 'ht' or lang.lower() == 'hat'):
		return 'ht'
	elif (lang.lower() == 'hausa' or lang.lower() == 'ha' or lang.lower() == 'hau'):
		return 'ha'
	elif (lang.lower() == 'hawaiian' or lang.lower() == 'haw'):
		return 'haw'
	elif (lang.lower() == 'hebrew' or lang.lower() == 'he' or lang.lower() == 'heb'):
		return 'he'
	elif (lang.lower() == 'hindi' or lang.lower() == 'hi' or lang.lower() == 'hin'):
		return 'hi'
	elif (lang.lower() == 'hmong' or lang.lower() == 'hmn'):
		return 'hmn'
	elif (lang.lower() == 'hungarian' or lang.lower() == 'hu' or lang.lower() == 'hun'):
		return 'hu'
	elif (lang.lower() == 'icelandic' or lang.lower() == 'is' or lang.lower() == 'isl' or lang.lower() == 'ice'):
		return 'is'
	elif (lang.lower() == 'igbo' or lang.lower() == 'ig' or lang.lower() == 'ibo'):
		return 'ig'
	elif (lang.lower() == 'indonesian' or lang.lower() == 'id' or lang.lower() == 'ind'):
		return 'id'
	elif (lang.lower() == 'irish' or lang.lower() == 'ga' or lang.lower() == 'gle'):
		return 'ga'
	elif (lang.lower() == 'italian' or lang.lower() == 'it' or lang.lower() == 'ita'):
		return 'it'
	elif (lang.lower() == 'japanese' or lang.lower() == 'ja' or lang.lower() == 'jpn'):
		return 'ja'
	elif (lang.lower() == 'javanese' or lang.lower() == 'jv' or lang.lower() == 'jav'):
		return 'jv'
	elif (lang.lower() == 'kannada' or lang.lower() == 'kn' or lang.lower() == 'kan'):
		return 'kn'
	elif (lang.lower() == 'kazakh' or lang.lower() == 'kk' or lang.lower() == 'kaz'):
		return 'kk'
	elif (lang.lower() == 'khmer' or lang.lower() == 'km' or lang.lower() == 'khm'):
		return 'km'
	elif (lang.lower() == 'korean' or lang.lower() == 'ko' or lang.lower() == 'kor'):
		return 'ko'
	elif (lang.lower() == 'kurdish' or lang.lower() == 'kurmanji' or lang.lower() == 'ku' or lang.lower() == 'kur'):
		return 'ku'
	elif (lang.lower() == 'kyrgyz' or lang.lower() == 'ky' or lang.lower() == 'kir'):
		return 'ky'
	elif (lang.lower() == 'lao' or lang.lower() == 'lo'):
		return 'lo'
	elif (lang.lower() == 'latin' or lang.lower() == 'la' or lang.lower() == 'lat'):
		return 'la'
	elif (lang.lower() == 'latvian' or lang.lower() == 'lv' or lang.lower() == 'lav'):
		return 'lv'
	elif (lang.lower() == 'lithuanian' or lang.lower() == 'lt' or lang.lower() == 'lit'):
		return 'lt'
	elif (lang.lower() == 'luxembourgish' or lang.lower() == 'lb' or lang.lower() == 'ltz'):
		return 'lb'
	elif (lang.lower() == 'macedonian' or lang.lower() == 'mk' or lang.lower() == 'mkd' or lang.lower() == 'mac'):
		return 'mk'
	elif (lang.lower() == 'malagasy' or lang.lower() == 'mg' or lang.lower() == 'mlg'):
		return 'mg'
	elif (lang.lower() == 'malay' or lang.lower() == 'ms' or lang.lower() == 'msa' or lang.lower() == 'may'):
		return 'ms'
	elif (lang.lower() == 'malayalam' or lang.lower() == 'ml' or lang.lower() == 'mal'):
		return 'ml'
	elif (lang.lower() == 'maltese' or lang.lower() == 'mt' or lang.lower() == 'mlt'):
		return 'mt'
	elif (lang.lower() == 'maori' or lang.lower() == 'mi' or lang.lower() == 'mao' or lang.lower() == 'mri'):
		return 'mi'
	elif (lang.lower() == 'marathi' or lang.lower() == 'mr' or lang.lower() == 'mar'):
		return 'mr'
	elif (lang.lower() == 'mongolian' or lang.lower() == 'mn' or lang.lower() == 'mon'):
		return 'mn'
	elif (lang.lower() == 'myanmar' or lang.lower() == 'burmese' or lang.lower() == 'my' or lang.lower() == 'mya' or lang.lower() == 'bur'):
		return 'my'
	elif (lang.lower() == 'nepali' or lang.lower() == 'ne' or lang.lower() == 'nep'):
		return 'ne'
	elif (lang.lower() == 'norwegian' or lang.lower() == 'no' or lang.lower() == 'nor'):
		return 'no'
	elif (lang.lower() == 'pashto' or lang.lower() == 'ps' or lang.lower() == 'pus'):
		return 'ps'
	elif (lang.lower() == 'persian' or lang.lower() == 'fa' or lang.lower() == 'fas' or lang.lower() == 'per'):
		return 'fa'
	elif (lang.lower() == 'polish' or lang.lower() == 'pl' or lang.lower() == 'pol'):
		return 'pl'
	elif (lang.lower() == 'portuguese' or lang.lower() == 'pt' or lang.lower() == 'por'):
		return 'pt'
	elif (lang.lower() == 'punjabi' or lang.lower() == 'pa' or lang.lower() == 'pan'):
		return 'pa'
	elif (lang.lower() == 'romanian' or lang.lower() == 'ro' or lang.lower() == 'ron' or lang.lower() == 'rum'):
		return 'ro'
	elif (lang.lower() == 'russian' or lang.lower() == 'ru' or lang.lower() == 'rus'):
		return 'ru'
	elif (lang.lower() == 'samoan' or lang.lower() == 'sm' or lang.lower() == 'smo'):
		return 'sm'
	elif (lang.lower() == 'scots gaelic' or lang.lower() == 'scottish gaelic' or lang.lower() == 'gaelic' or lang.lower() == 'gd' or lang.lower() == 'gla'):
		return 'gd'
	elif (lang.lower() == 'serbian' or lang.lower() == 'sr' or lang.lower() == 'srp'):
		return 'sr'
	elif (lang.lower() == 'sesotho' or lang.lower() == 'sotho' or lang.lower() == 'st' or lang.lower() == 'sot'):
		return 'st'
	elif (lang.lower() == 'shona' or lang.lower() == 'sn' or lang.lower() == 'sna'):
		return 'sn'
	elif (lang.lower() == 'sindhi' or lang.lower() == 'sd' or lang.lower() == 'snd'):
		return 'sd'
	elif (lang.lower() == 'sinhala' or lang.lower() == 'si' or lang.lower() == 'sin'):
		return 'si'
	elif (lang.lower() == 'slovak' or lang.lower() == 'sk' or lang.lower() == 'slk' or lang.lower() == 'slo'):
		return 'sk'
	elif (lang.lower() == 'slovenian' or lang.lower() == 'sl' or lang.lower() == 'slv'):
		return 'sl'
	elif (lang.lower() == 'somali' or lang.lower() == 'so' or lang.lower() == 'som'):
		return 'so'
	elif (lang.lower() == 'spanish' or lang.lower() == 'es' or lang.lower() == 'spa'):
		return 'es'
	elif (lang.lower() == 'sundanese' or lang.lower() == 'su' or lang.lower() == 'sun'):
		return 'su'
	elif (lang.lower() == 'swahili' or lang.lower() == 'sw' or lang.lower() == 'swa'):
		return 'sw'
	elif (lang.lower() == 'swedish' or lang.lower() == 'sv' or lang.lower() == 'swe'):
		return 'sv'
	elif (lang.lower() == 'tajik' or lang.lower() == 'tg' or lang.lower() == 'tgk'):
		return 'tg'
	elif (lang.lower() == 'tamil' or lang.lower() == 'ta' or lang.lower() == 'tam'):
		return 'ta'
	elif (lang.lower() == 'telugu' or lang.lower() == 'te' or lang.lower() == 'tel'):
		return 'te'
	elif (lang.lower() == 'thai' or lang.lower() == 'th' or lang.lower() == 'tha'):
		return 'th'
	elif (lang.lower() == 'turkish' or lang.lower() == 'tr' or lang.lower() == 'tur'):
		return 'tr'
	elif (lang.lower() == 'ukrainian' or lang.lower() == 'uk' or lang.lower() == 'ukr'):
		return 'uk'
	elif (lang.lower() == 'urdu' or lang.lower() == 'ur' or lang.lower() == 'urd'):
		return 'ur'
	elif (lang.lower() == 'uzbek' or lang.lower() == 'uz' or lang.lower() == 'uzb'):
		return 'uz'
	elif (lang.lower() == 'vietnamese' or lang.lower() == 'vi' or lang.lower() == 'vie'):
		return 'vi'
	elif (lang.lower() == 'welsh' or lang.lower() == 'cy' or lang.lower() == 'cym' or lang.lower() == 'wel'):
		return 'cy'
	elif (lang.lower() == 'xhosa' or lang.lower() == 'xh' or lang.lower() == 'xho'):
		return 'xh'
	elif (lang.lower() == 'yiddish' or lang.lower() == 'yi' or lang.lower() == 'yid'):
		return 'yi'
	elif (lang.lower() == 'yoruba' or lang.lower() == 'yo' or lang.lower() == 'yor'):
		return 'yo'
	elif (lang.lower() == 'zulu' or lang.lower() == 'zu' or lang.lower() == 'zul'):
		return 'zu'
	else:
		print('Language not supported')
		sys.exit()
