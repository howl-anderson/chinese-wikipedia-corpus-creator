#!/bin/bash

WikiExtractor.py --json raw_data/zhwiki-latest-pages-articles.xml.bz2 -o extracted_json_data --processes 8
