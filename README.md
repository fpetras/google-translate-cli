# google-translate-cli
A command-line interface for Google Translate, using Python and the Google Cloud Translation API

## Setup:

```
# Install google-cloud-translate and google-cloud-texttospeech:
pip install google-cloud-translate==1.3.1
pip install google-cloud-texttospeech==0.2.0

# To enable spell checking in interactive mode, install pyspellchecker:
pip install pyspellchecker
# in case of error or if it doesn't work, install from my modified source:
git clone https://github.com/fpetras/[TODO].git && cd [TODO] && python setup.py install

# Add path to credential .json file to the environment:
export GOOGLE_APPLICATION_CREDENTIALS=[PATH]
# See instructions.txt for how to generate a credentials .json file

# OR alternatively, use 2translate.py, which uses googletrans, a free and unlimited python library that implemented the Google Translate API
# Install googletrans:
pip install googletrans

```

## Usage:

`usage: ./translate.py "Text to translate" "Target language"`

```
usage: ./translate.py [options] [Input to translate] [target language [...]]

optional arguments:
  -h, --help         show this help message and exit
  -c, --confidence   display detected language confidence level
  -s, --speech       text-to-speech
  -f, --file FILE    translate FILE
  -u, --url          translate web page (opens browser)
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
     Bengali        - bn   │ Irish          - ga   │ Serbian        - sr   
     Bosnian        - bs   │ Italian        - it  *│ Sesotho        - st   
     Bulgarian      - bg   │ Japanese       - ja  *│ Shona          - sn   
     Catalan        - ca   │ Javanese       - jv   │ Sindhi         - sd   
     Cebuano        - ceb  │ Kannada        - kn   │ Sinhala        - si   
     Chichewa       - ny   │ Kazakh         - kk   │ Slovak         - sk  *
     Chinese Simp.  - zh-CN│ Khmer          - km   │ Slovenian      - sl   
     Chinese Trad.  - zh-TW│ Korean         - ko  *│ Somali         - so   
     Corsican       - co   │ Kurdish        - ku   │ Spanish        - es  *
     Croatian       - hr   │ Kyrgyz         - ky   │ Sundanese      - su   
     Czech          - cs   │ Lao            - lo   │ Swahili        - sw   
     Danish         - da  *│ Latin          - la   │ Swedish        - sv  *
     Dutch          - nl  *│ Latvian        - lv   │ Tajik          - tg   
     English        - en  *│ Lithuanian     - lt   │ Tamil          - ta   
     Esperanto      - eo   │ Luxembourgish  - lb   │ Telugu         - te   
     Estonian       - et   │ Macedonian     - mk   │ Thai           - th   
     Filipino       - fil  │ Malagasy       - mg   │ Turkish        - tr  *
     Finnish        - fi   │ Malay          - ms   │ Ukrainian      - uk   
     French         - fr  *│ Malayalam      - ml   │ Urdu           - ur   
     Frisian        - fry  │ Maltese        - mt   │ Uzbek          - uz   
     Galician       - gl   │ Maori          - mi   │ Vietnamese     - vi   
     Georgian       - ka   │ Marathi        - mr   │ Welsh          - cy   
     German         - de  *│ Mongolian      - mn   │ Xhosa          - xh   
     Greek          - el   │ Myanmar        - my   │ Yiddish        - yi   
     Gujarati       - gu   │ Nepali         - ne   │ Yoruba         - yo   
     Haitian Creole - ht   │ Norwegian      - no   │ Zulu           - zu   
     Hausa          - ha   │ Pashto         - ps   │                       
\* indicates support for text-to-speech

Both ISO 639-1, 639-2, and the full language name are supported

Interactive mode spell-checks the language entry
