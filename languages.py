# -*- coding: utf-8 -*-

def languages(lang):
	if (lang.lower() == 'afrikaans' or lang.lower() == 'af' or lang.lower() == 'afr'):
		return 'af'
	elif (lang.lower() == 'albanian' or lang.lower() == 'shqip' or lang.lower() == 'sq' or lang.lower() == 'sqi' or lang.lower() == 'alb'):
		return 'sq'
	elif (lang.lower() == 'amharic' or lang.decode('utf-8') == u'አማርኛ' or lang.lower() == 'am' or lang.lower() == 'amh'):
		return 'am'
	elif (lang.lower() == 'arabic' or lang.decode('utf-8') == u'العربية' or lang.lower() == 'ar' or lang.lower() == 'ara'):
		return 'ar'
	elif (lang.lower() == 'armenian' or lang.decode('utf-8') == u'Հայերեն' or lang.lower() == 'hy' or lang.lower() == 'arm' or lang.lower() == 'hye'):
		return 'hy'
	elif (lang.lower() == 'azerbaijani' or lang.lower().decode('utf-8') == u'azərbaycanca' or lang.lower() == 'az' or lang.lower() == 'aze'):
		return 'az'
	elif (lang.lower() == 'basque' or lang.lower() == 'euskara' or lang.lower() == 'eu' or lang.lower() == 'eur' or lang.lower() == 'baq'):
		return 'eu'
	elif (lang.lower() == 'belarusian' or lang.decode('utf-8') == u'беларуская' or lang.lower() == 'be' or lang.lower() == 'bel'):
		return 'be'
	elif (lang.lower() == 'bengali' or lang.decode('utf-8') == u'বাংলা' or lang.lower() == 'bn' or lang.lower() == 'ben'):
		return 'bn'
	elif (lang.lower() == 'bosnian' or lang.lower() == 'bosanski' or lang.lower() == 'bs' or lang.lower() == 'bos'):
		return 'bs'
	elif (lang.lower() == 'bulgarian' or lang.decode('utf-8') == u'български' or lang.lower() == 'bg' or lang.lower() == 'bul'):
		return 'bg'
	elif (lang.lower() == 'catalan' or lang.lower().decode('utf-8') == u'català' or lang.lower() == 'catala' or lang.lower() == 'cat'):
		return 'ca'
	elif (lang.lower() == 'cebuano' or lang.lower() == 'ceb'):
		return 'ceb'
	elif (lang.lower() == 'chichewa' or lang.lower() == 'nyanja' or lang.lower() == 'ny' or lang.lower() == 'nya'):
		return 'ny'
	elif (lang.lower() == 'chinese' or lang.decode('utf-8') == u'简体中文' or lang.lower() == 'zh' or lang.lower() == 'zho' or lang.lower() == 'chi' or lang.lower() == 'zh-cn'):
		return 'zh'
	elif (lang.lower() == 'zh-tw' or lang.decode('utf-8') == u'正體中文'):
		return 'zh-TW'
	elif (lang.lower() == 'corsican' or lang.lower() == 'corsu' or lang.lower() == 'co' or lang.lower() == 'cos'):
		return 'co'
	elif (lang.lower() == 'croatian' or lang.lower() == 'hrvatski' or lang.lower() == 'hr' or lang.lower() == 'hrw'):
		return 'hr'
	elif (lang.lower() == 'czech' or lang.lower().decode('utf-8') == u'čeština' or lang.lower() == 'cestina' or lang.lower() == 'cs' or lang.lower() == 'ces' or lang.lower() == 'cze'):
		return 'cs'
	elif (lang.lower() == 'danish' or lang.lower() == 'dansk' or lang.lower() == 'da' or lang.lower() == 'dan'):
		return 'da'
	elif (lang.lower() == 'dutch' or lang.lower() == 'nederlands' or lang.lower() == 'nl' or lang.lower() == 'nld' or lang.lower() == 'dut'):
		return 'nl'
	elif (lang.lower() == 'english' or lang.lower() == 'en' or lang.lower() == 'eng'):
		return 'en'
	elif (lang.lower() == 'esperanto' or lang.lower() == 'eo' or lang.lower() == 'epo'):
		return 'eo'
	elif (lang.lower() == 'estonian' or lang.lower() == 'eesti' or lang.lower() == 'et' or lang.lower() == 'est'):
		return 'et'
	elif (lang.lower() == 'filipino' or lang.lower() == 'tagalog' or lang.lower() == 'tl' or lang.lower() == 'fil'):
		return 'tl'
	elif (lang.lower() == 'finnish' or lang.lower() == 'suomi' or lang.lower() == 'fi' or lang.lower() == 'fin'):
		return 'fi'
	elif (lang.lower() == 'french' or lang.lower().decode('utf-8') == u'français' or lang.lower() == 'francais' or lang.lower() == 'fr' or lang.lower() == 'fre' or lang.lower() == 'fra'):
		return 'fr'
	elif (lang.lower() == 'frisian' or lang.lower() == 'frysk' or lang.lower() == 'fy' or lang.lower() == 'fry' or lang.lower() == 'frr' or lang.lower() == 'frs'):
		return 'fy'
	elif (lang.lower() == 'galician' or lang.lower() == 'galego' or lang.lower() == 'gl' or lang.lower() == 'glg'):
		return 'gl'
	elif (lang.lower() == 'georgian' or lang.decode('utf-8') == u'ქართული' or lang.lower() == 'ka' or lang.lower() == 'kat' or lang.lower() == 'geo'):
		return 'ka'
	elif (lang.lower() == 'german' or lang.lower() == 'deutsch' or lang.lower() == 'de' or lang.lower() == 'deu' or lang.lower() == 'ger'):
		return 'de'
	elif (lang.lower() == 'greek' or lang.decode('utf-8') == u'Ελληνικά' or lang.lower() == 'el' or lang.lower() == 'ell' or lang.lower() == 'gre'):
		return 'el'
	elif (lang.lower() == 'gujarati' or lang.decode('utf-8') == u'ગુજરાતી' or lang.lower() == 'gu' or lang.lower() == 'guj'):
		return 'gu'
	elif (lang.lower() == 'haitian creole' or lang.lower().decode('utf-8') == u'kreyòl ayisyen' or lang.lower() == 'kreyol ayisyen' or lang.lower() == 'haitian' or lang.lower() == 'ht' or lang.lower() == 'hat'):
		return 'ht'
	elif (lang.lower() == 'hausa' or lang.lower() == 'ha' or lang.lower() == 'hau'):
		return 'ha'
	elif (lang.lower() == 'hawaiian' or lang.lower().decode('utf-8') == u'ʻōlelo hawaiʻi' or lang.lower() == 'haw'):
		return 'haw'
	elif (lang.lower() == 'hebrew' or lang.decode('utf-8') == u'עִבְרִית' or lang.lower() == 'he' or lang.lower() == 'heb'):
		return 'he'
	elif (lang.lower() == 'hindi' or lang.decode('utf-8') == u'हिन्दी' or lang.lower() == 'hi' or lang.lower() == 'hin'):
		return 'hi'
	elif (lang.lower() == 'hmong' or lang.lower() == 'hmoob' or lang.lower() == 'hmn'):
		return 'hmn'
	elif (lang.lower() == 'hungarian' or lang.lower() == 'magyar' or lang.lower() == 'hu' or lang.lower() == 'hun'):
		return 'hu'
	elif (lang.lower() == 'icelandic' or lang.lower().decode('utf-8') == u'íslenska' or lang.lower() == 'islenska' or lang.lower() == 'is' or lang.lower() == 'isl' or lang.lower() == 'ice'):
		return 'is'
	elif (lang.lower() == 'igbo' or lang.lower() == 'ig' or lang.lower() == 'ibo'):
		return 'ig'
	elif (lang.lower() == 'indonesian' or lang.lower() == 'bahasa indonesia' or lang.lower() == 'id' or lang.lower() == 'ind'):
		return 'id'
	elif (lang.lower() == 'irish' or lang.lower() == 'gaeilge' or lang.lower() == 'ga' or lang.lower() == 'gle'):
		return 'ga'
	elif (lang.lower() == 'italian' or lang.lower() == 'italiano' or lang.lower() == 'it' or lang.lower() == 'ita'):
		return 'it'
	elif (lang.lower() == 'japanese' or lang.decode('utf-8') == u'日本語' or lang.lower() == 'ja' or lang.lower() == 'jpn'):
		return 'ja'
	elif (lang.lower() == 'javanese' or lang.lower() == 'basa jawa' or lang.lower() == 'jv' or lang.lower() == 'jav'):
		return 'jv'
	elif (lang.lower() == 'kannada' or lang.decode('utf-8') == u'ಕನ್ನಡ' or lang.lower() == 'kn' or lang.lower() == 'kan'):
		return 'kn'
	elif (lang.lower() == 'kazakh' or lang.decode('utf-8') == u'Қазақ тілі' or lang.lower() == 'kk' or lang.lower() == 'kaz'):
		return 'kk'
	elif (lang.lower() == 'khmer' or lang.decode('utf-8') == u'ភាសាខ្មែរ' or lang.lower() == 'km' or lang.lower() == 'khm'):
		return 'km'
	elif (lang.lower() == 'korean' or lang.decode('utf-8') == u'한국어' or lang.lower() == 'ko' or lang.lower() == 'kor'):
		return 'ko'
	elif (lang.lower() == 'kurdish' or lang.lower().decode('utf-8') == u'kurdî' or lang.lower() == 'kurdi' or lang.lower() == 'kurmanji' or lang.lower() == 'ku' or lang.lower() == 'kur'):
		return 'ku'
	elif (lang.lower() == 'kyrgyz' or lang.decode('utf-8') == u'Кыргызча' or lang.lower() == 'ky' or lang.lower() == 'kir'):
		return 'ky'
	elif (lang.lower() == 'lao' or lang.decode('utf-8') == u'ລາວ' or lang.lower() == 'lo'):
		return 'lo'
	elif (lang.lower() == 'latin' or lang.lower() == 'latina' or lang.lower() == 'la' or lang.lower() == 'lat'):
		return 'la'
	elif (lang.lower() == 'latvian' or lang.lower().decode('utf-8') == u'latviešu' or lang.lower() == 'latviesu' or lang.lower() == 'lv' or lang.lower() == 'lav'):
		return 'lv'
	elif (lang.lower() == 'lithuanian' or lang.lower().decode('utf-8') == u'lietuvių' or lang.lower() == 'lietuviu' or lang.lower() == 'lt' or lang.lower() == 'lit'):
		return 'lt'
	elif (lang.lower() == 'luxembourgish' or lang.lower().decode('utf-8') == u'lëtzebuergesch' or lang.lower() == 'letzebuergesch' or lang.lower() == 'lb' or lang.lower() == 'ltz'):
		return 'lb'
	elif (lang.lower() == 'macedonian' or lang.decode('utf-8') == u'Македонски' or lang.lower() == 'mk' or lang.lower() == 'mkd' or lang.lower() == 'mac'):
		return 'mk'
	elif (lang.lower() == 'malagasy' or lang.lower() == 'mg' or lang.lower() == 'mlg'):
		return 'mg'
	elif (lang.lower() == 'malay' or lang.lower() == 'bahasa melayu' or lang.lower() == 'ms' or lang.lower() == 'msa' or lang.lower() == 'may'):
		return 'ms'
	elif (lang.lower() == 'malayalam' or lang.decode('utf-8') == u'മലയാളം' or lang.lower() == 'ml' or lang.lower() == 'mal'):
		return 'ml'
	elif (lang.lower() == 'maltese' or lang.lower() == 'malti' or lang.lower() == 'mt' or lang.lower() == 'mlt'):
		return 'mt'
	elif (lang.lower() == 'maori' or lang.lower().decode('utf-8') == u'māori' or lang.lower() == 'mi' or lang.lower() == 'mao' or lang.lower() == 'mri'):
		return 'mi'
	elif (lang.lower() == 'marathi' or lang.decode('utf-8') == u'मराठी' or lang.lower() == 'mr' or lang.lower() == 'mar'):
		return 'mr'
	elif (lang.lower() == 'mongolian' or lang.decode('utf-8') == u'Монгол' or lang.lower() == 'mn' or lang.lower() == 'mon'):
		return 'mn'
	elif (lang.lower() == 'myanmar' or lang.decode('utf-8') == u'မြန်မာစာ' or lang.lower() == 'burmese' or lang.lower() == 'my' or lang.lower() == 'mya' or lang.lower() == 'bur'):
		return 'my'
	elif (lang.lower() == 'nepali' or lang.decode('utf-8') == u'नेपाली'or lang.lower() == 'ne' or lang.lower() == 'nep'):
		return 'ne'
	elif (lang.lower() == 'norwegian' or lang.lower() == 'norsk' or lang.lower() == 'no' or lang.lower() == 'nor'):
		return 'no'
	elif (lang.lower() == 'pashto' or lang.decode('utf-8') == u'پښتو' or lang.lower() == 'ps' or lang.lower() == 'pus'):
		return 'ps'
	elif (lang.lower() == 'persian' or lang.lower() == 'farsi' or lang.decode('utf-8') == u'فارسی' or lang.lower() == 'fa' or lang.lower() == 'fas' or lang.lower() == 'per'):
		return 'fa'
	elif (lang.lower() == 'polish' or lang.lower() == 'polski' or lang.lower() == 'pl' or lang.lower() == 'pol'):
		return 'pl'
	elif (lang.lower() == 'portuguese' or lang.lower().decode('utf-8') == u'português' or lang.lower() == 'portugues' or lang.lower() == 'pt' or lang.lower() == 'por'):
		return 'pt'
	elif (lang.lower() == 'punjabi' or lang.decode('utf-8') == u'ਪੰਜਾਬੀ' or lang.lower() == 'pa' or lang.lower() == 'pan'):
		return 'pa'
	elif (lang.lower() == 'romanian' or lang.lower().decode('utf-8') == u'română' or lang.lower() == 'romana' or lang.lower() == 'ro' or lang.lower() == 'ron' or lang.lower() == 'rum'):
		return 'ro'
	elif (lang.lower() == 'russian' or lang.decode('utf-8') == u'Русский' or lang.lower() == 'ru' or lang.lower() == 'rus'):
		return 'ru'
	elif (lang.lower() == 'samoan' or lang.lower().decode('utf-8') == u'gagana sāmoa' or lang.lower() == 'gagana samoa' or lang.lower() == 'sm' or lang.lower() == 'smo'):
		return 'sm'
	elif (lang.lower() == 'scots gaelic' or lang.lower() == 'scottish gaelic' or lang.lower() == 'gaelic' or lang.lower().decode('utf-8') == u'gàidhlig' or lang.lower() == 'gaidhlig' or lang.lower() == 'gd' or lang.lower() == 'gla'):
		return 'gd'
	elif (lang.lower() == 'serbian' or lang.decode('utf-8') == u'српски' or lang.lower() == 'sr' or lang.lower() == 'srp' or lang.lower() == 'sr-cy' or lang.lower() == 'sr-cyrl'):
		return 'sr'
	elif (lang.lower() == 'srpski' or lang.lower() == 'sr-la' or lang.lower() == 'sr-latn'):
		return 'sr-Latn'
	elif (lang.lower() == 'sesotho' or lang.lower() == 'sotho' or lang.lower() == 'st' or lang.lower() == 'sot'):
		return 'st'
	elif (lang.lower() == 'shona' or lang.lower() == 'chishona' or lang.lower() == 'sn' or lang.lower() == 'sna'):
		return 'sn'
	elif (lang.lower() == 'sindhi' or lang.decode('utf-8') == u'سنڌي' or lang.lower() == 'sd' or lang.lower() == 'snd'):
		return 'sd'
	elif (lang.lower() == 'sinhala' or lang.decode('utf-8') == u'සිංහල' or lang.lower() == 'si' or lang.lower() == 'sin'):
		return 'si'
	elif (lang.lower() == 'slovak' or lang.lower().decode('utf-8') == u'slovenčina' or lang.lower() == 'slovencina' or lang.lower() == 'sk' or lang.lower() == 'slk' or lang.lower() == 'slo'):
		return 'sk'
	elif (lang.lower() == 'slovenian' or lang.lower().decode('utf-8') == u'slovenščina' or lang.lower() == 'slovenscina' or lang.lower() == 'sl' or lang.lower() == 'slv'):
		return 'sl'
	elif (lang.lower() == 'somali' or lang.lower() == 'soomaali' or lang.lower() == 'so' or lang.lower() == 'som'):
		return 'so'
	elif (lang.lower() == 'spanish' or lang.lower().decode('utf-8') == u'español' or lang.lower() == 'espanol' or lang.lower() == 'es' or lang.lower() == 'spa'):
		return 'es'
	elif (lang.lower() == 'sundanese' or lang.lower() == 'basa sunda' or lang.lower() == 'su' or lang.lower() == 'sun'):
		return 'su'
	elif (lang.lower() == 'swahili' or lang.lower() == 'kiswahili' or lang.lower() == 'sw' or lang.lower() == 'swa'):
		return 'sw'
	elif (lang.lower() == 'swedish' or lang.lower() == 'svenska' or lang.lower() == 'sv' or lang.lower() == 'swe'):
		return 'sv'
	elif (lang.lower() == 'tajik' or lang.decode('utf-8') == u'Тоҷикӣ' or lang.lower() == 'tg' or lang.lower() == 'tgk'):
		return 'tg'
	elif (lang.lower() == 'tamil' or lang.decode('utf-8') == u'தமிழ்' or lang.lower() == 'ta' or lang.lower() == 'tam'):
		return 'ta'
	elif (lang.lower() == 'telugu' or lang.decode('utf-8') == u'తెలుగు' or lang.lower() == 'te' or lang.lower() == 'tel'):
		return 'te'
	elif (lang.lower() == 'thai' or lang.decode('utf-8') == u'ไทย' or lang.lower() == 'th' or lang.lower() == 'tha'):
		return 'th'
	elif (lang.lower() == 'turkish' or lang.lower().decode('utf-8') == u'türkçe' or lang.lower() == 'turkce' or lang.lower() == 'tr' or lang.lower() == 'tur'):
		return 'tr'
	elif (lang.lower() == 'ukrainian' or lang.decode('utf-8') == u'Українська' or lang.lower() == 'uk' or lang.lower() == 'ukr'):
		return 'uk'
	elif (lang.lower() == 'urdu' or lang.decode('utf-8') == u'اُردُو' or lang.lower() == 'ur' or lang.lower() == 'urd'):
		return 'ur'
	elif (lang.lower() == 'uzbek' or lang.lower().decode('utf-8') == u'oʻzbek tili' or lang.lower() == 'uz' or lang.lower() == 'uzb'):
		return 'uz'
	elif (lang.lower() == 'vietnamese' or lang.lower().decode('utf-8') == u'tiếng việt' or lang.lower() == 'tieng viet' or lang.lower() == 'vi' or lang.lower() == 'vie'):
		return 'vi'
	elif (lang.lower() == 'welsh' or lang.lower() == 'cymraeg' or lang.lower() == 'cy' or lang.lower() == 'cym' or lang.lower() == 'wel'):
		return 'cy'
	elif (lang.lower() == 'xhosa' or lang.lower() == 'isixhosa' or lang.lower() == 'xh' or lang.lower() == 'xho'):
		return 'xh'
	elif (lang.lower() == 'yiddish' or lang.decode('utf-8') == u'ייִדיש' or lang.lower() == 'yi' or lang.lower() == 'yid'):
		return 'yi'
	elif (lang.lower() == 'yoruba' or lang.lower().decode('utf-8') == u'yorùbá' or lang.lower() == 'yo' or lang.lower() == 'yor'):
		return 'yo'
	elif (lang.lower() == 'zulu' or lang.lower() == 'isizulu' or lang.lower() == 'zu' or lang.lower() == 'zul'):
		return 'zu'
	else:
		return False
