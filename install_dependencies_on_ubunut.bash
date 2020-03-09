#!/usr/bin/env bash

sudo apt install -y opencc git
python ./get_wikiextractor.py
pip3 install -r requirements.txt
