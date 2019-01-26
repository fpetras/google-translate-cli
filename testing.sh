#!/bin/bash
set -x
./translate.py "This is a simple text" fr
./translate.py "Übersetze mich"
./translate.py -c "This test is going well" de -s
./translate.py -s "Many different languages" fr japanese et zh-CN zulu Amharic
./translate.py -f /dev/urandom es pt
./translate.py -c -s -f test NaL jp
./translate.py -s "Dieser Test scheint gut gelaufen zu sein" en
