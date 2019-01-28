#!/bin/bash

set -x
./translate.py "This is a simple text" fr
./translate.py "Übersetze mich"
./translate.py -c "This test is going well so far" de -s
./translate.py -s "Many different languages" fr japanese et zh-CN zulu Amharic
./translate.py -f /dev/urandom es pt
./translate.py -c -s -f file NaL ja
./translate.py -s "Dieser Test scheint bisher gut gelaufen zu sein" en
./translate.py -b "Testing bare output" ice
./translate.py "Testing bare output again" German --bare
./translate.py "Testing spell checking" englsh geman portugiese
./translate.py -c "Native language names" ქართული ייִדיש ລາວ 한국어 Slovenščina
./translate.py "Randomness" rng rng rng rng
./translate.py --url news.ycombinator.com Français
