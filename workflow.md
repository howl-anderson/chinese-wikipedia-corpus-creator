# Processing workflow

## Downloading raw data
    * input：-
    * output：`raw_data/*wiki-latest-pages-articles.xml.bz2`
    * script：`download_wikipedia_raw_corpus.bash`

## Extracting content
    * input：`raw_data/zhwiki-latest-pages-articles.xml.bz2`
    * output：`extracted_json_data/**/*`
    * script：`extract_wikipedia_json_corpus.bash`

## Convert to plain text
    * input：`extracted_json_data/**/*`
    * output：`spacy_standard_plain_files/*`
    * script：`json_corpus_to_plain_text.bash`

## Convert traditional chinese to simplified chinese
    * input：`spacy_standard_plain_files/*`
    * output：`normaled_plain_files/*`
    * script：`normal_text.bash`

## Splitting sentence and clean up empty lines
    * input：`normaled_plain_files/*`
    * output：`sentence_data/*`
    * script：`split_text_to_sentence.bash`

## Tokenizer
    * input：`sentence_data/*`
    * output：`token_cleaned_plain_files/*`
    * script：`token_plain_text.bash`
