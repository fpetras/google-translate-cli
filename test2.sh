#!/bin/bash

set -x
./v2-translate.py "This is a simple text" fr
./v2-translate.py "Übersetze mich"
./v2-translate.py -c "This test is going well" de -s
./v2-translate.py  "Many different languages" fr japanese et zh-CN zulu Amharic
./v2-translate.py -f /dev/urandom es pt
./v2-translate.py -c -f test NaL ja
./v2-translate.py "Dieser Test scheint bisher gut gelaufen zu sein" en
./v2-translate.py -b "Testing bare output" ice
./v2-translate.py "Testing bare output again" German --bare
./v2-translate.py "Testing spell checking" englsh geman portugiese
./v2-translate.py -c "Native language names" ქართული ייִדיש ລາວ 한국어 Slovenščina
./v2-translate.py --url news.ycombinator.com Français
