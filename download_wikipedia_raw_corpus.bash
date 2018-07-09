#!/bin/bash

# download the latest Chinese wikipedia dump
file=raw_data/zhwiki-latest-pages-articles.xml.bz2
if [ ! -f "$file" ]; then
    wget -O ${file} -c "https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2"
fi
