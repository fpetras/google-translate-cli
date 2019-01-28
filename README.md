# google-translate-cli
A command-line interface for Google Translate, using Python and the Google Cloud Translation API

## Setup:

```
# Install google-cloud-translate and google-cloud-texttospeech:
pip install -r requirements.txt

# To enable language name spell checking and autocorrection, install pyspellchecker:
pip install pyspellchecker
# in case of error or nonfunctioning, install from my modified source:
git clone https://github.com/fpetras/pyspellchecker.git && cd pyspellchecker && python setup.py install

# Add path to credential .json file to the environment:
export GOOGLE_APPLICATION_CREDENTIALS=[PATH]
# See instructions.txt on how to generate a credentials .json file

# OR alternatively, use v2-translate.py, which uses the library googletrans
# (unlimited API calls, but less stable, less functionality, and may stop working at any time)
# Install googletrans:
pip install googletrans

```

## Usage:

```
usage: ./translate.py [options] [Input to translate] [target language [...]]

optional arguments:
  -h, --help         show this help message and exit
  -l, --language     print supported languages and exit
  -b, --bare         output the bare translation
  -c, --confidence   display detected language confidence level
  -s, --speech       activate text-to-speech
  -f, --file FILE    translate FILE
  -u, --url URL      translate web page (opens browser)
  -i, --interactive  interactive mode
```

## Supported languages:


     Afrikaans      - af   │ Hawaiian       - haw  │ Persian        - fa   
     Albanian       - sq   │ Hebrew         - he   │ Polish         - pl   
     Amharic        - am   │ Hindi          - hi   │ Portuguese     - pt  *
     Arabic         - ar   │ Hmong          - hmv  │ Punjabi        - pa   
     Armenian       - hy   │ Hungarian      - hu   │ Romanian       - ro   
     Azerbaijani    - az   │ Icelandic      - is   │ Russian        - ru  *
     Basque         - eu   │ Igbo           - ig   │ Samoan         - sm   
     Belarusian     - be   │ Indonesian     - id   │ Scots Gaelic   - gd   
     Bengali        - bn   │ Irish          - ga   │ Serbian Cyril. - sr-CY
     Bosnian        - bs   │ Italian        - it  *│ Serbian Latin  - sr-LA
     Bulgarian      - bg   │ Japanese       - ja  *│ Sesotho        - st   
     Catalan        - ca   │ Javanese       - jv   │ Shona          - sn   
     Cebuano        - ceb  │ Kannada        - kn   │ Sindhi         - sd   
     Chichewa       - ny   │ Kazakh         - kk   │ Sinhala        - si   
     Chinese Simp.  - zh-CN│ Khmer          - km   │ Slovak         - sk  *
     Chinese Trad.  - zh-TW│ Korean         - ko  *│ Slovenian      - sl   
     Corsican       - co   │ Kurdish        - ku   │ Somali         - so   
     Croatian       - hr   │ Kyrgyz         - ky   │ Spanish        - es  *
     Czech          - cs   │ Lao            - lo   │ Sundanese      - su   
     Danish         - da  *│ Latin          - la   │ Swahili        - sw   
     Dutch          - nl  *│ Latvian        - lv   │ Swedish        - sv  *
     English        - en  *│ Lithuanian     - lt   │ Tajik          - tg   
     Esperanto      - eo   │ Luxembourgish  - lb   │ Tamil          - ta   
     Estonian       - et   │ Macedonian     - mk   │ Telugu         - te   
     Filipino       - fil  │ Malagasy       - mg   │ Thai           - th   
     Finnish        - fi   │ Malay          - ms   │ Turkish        - tr  *
     French         - fr  *│ Malayalam      - ml   │ Ukrainian      - uk   
     Frisian        - fy   │ Maltese        - mt   │ Urdu           - ur   
     Galician       - gl   │ Maori          - mi   │ Uzbek          - uz   
     Georgian       - ka   │ Marathi        - mr   │ Vietnamese     - vi   
     German         - de  *│ Mongolian      - mn   │ Welsh          - cy   
     Greek          - el   │ Myanmar        - my   │ Xhosa          - xh   
     Gujarati       - gu   │ Nepali         - ne   │ Yiddish        - yi   
     Haitian Creole - ht   │ Norwegian      - no   │ Yoruba         - yo   
     Hausa          - ha   │ Pashto         - ps   │ Zulu           - zu   

\* indicates support for text-to-speech

Supports ISO 639-1, 639-2, English and native language names

English language name entries are spell-checked and autocorrected
