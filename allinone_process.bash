#!/usr/bin/env bash

./download_wikipedia_raw_corpus.bash
./extract_wikipedia_json_corpus.bash
./json_corpus_to_plain_text.bash
./normal_text.bash
./split_text_to_sentence.bash
./token_plain_text.bash