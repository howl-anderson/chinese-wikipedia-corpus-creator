#!/bin/bash

# download the latest English wikipedia dump
wget -O raw_data/enwiki-latest-pages-articles.xml.bz2 -c "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"

# download the latest English wikipedia dump
wget -O raw_data/zhwiki-latest-pages-articles.xml.bz2 -c "https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2"
