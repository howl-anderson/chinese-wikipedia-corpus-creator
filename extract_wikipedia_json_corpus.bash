#!/bin/bash

cpu_count=`nproc --all`
process_count=$(expr $cpu_count - 1)
python ./WikiExtractor.py --json raw_data/zhwiki-latest-pages-articles.xml.bz2 -o extracted_json_data --processes ${process_count}
