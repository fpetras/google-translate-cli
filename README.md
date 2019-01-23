# google-translate-cli
A command-line interface for Google Translate

## Setup:

```
sudo pip install --upgrade google-cloud-translate==1.3.1
# install gcloud
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
# go to https://console.cloud.google.com/apis/credentials?project=[PROJECT_ID]
# or run
gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"

gcloud iam service-accounts keys create [KEY_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```

## Usage:

`usage: ./translate.py "Text to translate" "Target language"`

Supported languages:
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
    └───────────────────────┴───────────────────────┴───────────────────────┘

Both ISO 639-1 and the full language name are supported
