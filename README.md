# google-translate-cli
A command-line interface for Google Translate, using Python and the Google Cloud Translation API

## Setup:

```
# Install google-cloud-translate:
sudo pip install --upgrade google-cloud-translate==1.3.1
# Install gcloud:
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
# Generate credential .json file:
# go to https://console.cloud.google.com/apis/credentials?project=[PROJECT_ID]
# or run
gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"
gcloud iam service-accounts keys create [KEY_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com
# Add path to credential .json file to the environment:
export GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```

## Usage:

`usage: ./translate.py "Text to translate" "Target language"`

Supported languages:

     Afrikaans      - af   │ Hebrew         - he   │ Polish         - pl   
     Albanian       - sq   │ Hindi          - hi   │ Portuguese     - pt   
     Amharic        - am   │ Hmong          - hmv  │ Punjabi        - pa   
     Arabic         - ar   │ Hungarian      - hu   │ Romanian       - ro   
     Armenian       - hy   │ Icelandic      - is   │ Russian        - ru   
     Azerbaijani    - az   │ Igbo           - ig   │ Samoan         - sm   
     Basque         - eu   │ Indonesian     - id   │ Scots Gaelic   - gd   
     Belarusian     - be   │ Irish          - ga   │ Serbian        - sr   
     Bengali        - bn   │ Italian        - it   │ Sesotho        - st   
     Bosnian        - bs   │ Japanese       - ja   │ Shona          - sn   
     Bulgarian      - bg   │ Javanese       - jv   │ Sindhi         - sd   
     Catalan        - ca   │ Kannada        - kn   │ Sinhala        - si   
     Cebuano        - ceb  │ Kazakh         - kk   │ Slovak         - sk   
     Chichewa       - ny   │ Khmer          - km   │ Slovenian      - sl   
     Chinese        - zh   │ Korean         - ko   │ Somali         - so   
     Corsican       - co   │ Kurdish        - ku   │ Spanish        - es   
     Croatian       - hr   │ Kyrgyz         - ky   │ Sundanese      - su   
     Czech          - cs   │ Lao            - lo   │ Swahili        - sw   
     Danish         - da   │ Latin          - la   │ Swedish        - sv   
     Dutch          - nl   │ Latvian        - lv   │ Tajik          - tg   
     English        - en   │ Lithuanian     - lt   │ Tamil          - ta   
     Esperanto      - eo   │ Luxembourgish  - lb   │ Telugu         - te   
     Estonian       - et   │ Macedonian     - mk   │ Thai           - th   
     Filipino       - fil  │ Malagasy       - mg   │ Turkish        - tr   
     Finnish        - fi   │ Malay          - ms   │ Ukrainian      - uk   
     French         - fr   │ Malayalam      - ml   │ Urdu           - ur   
     Frisian        - fry  │ Maltese        - mt   │ Uzbek          - uz   
     Galician       - gl   │ Maori          - mi   │ Vietnamese     - vi   
     Georgian       - ka   │ Marathi        - mr   │ Welsh          - cy   
     German         - de   │ Mongolian      - mn   │ Xhosa          - xh   
     Greek          - el   │ Myanmar        - my   │ Yiddish        - yi   
     Gujarati       - gu   │ Nepali         - ne   │ Yoruba         - yo   
     Haitian Creole - ht   │ Norwegian      - no   │ Zulu           - zu   
     Hausa          - ha   │ Pashto         - ps   │                       
     Hawaiian       - haw  │ Persian        - fa   │                       
     
Both ISO 639-1, 639-2, and the full language name are supported
