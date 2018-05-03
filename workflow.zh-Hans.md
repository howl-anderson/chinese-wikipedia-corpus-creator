# 语料库处理流程

## 下载原始文档
   * 输入：-
   * 输出：`raw_data/*wiki-latest-pages-articles.xml.bz2`
   * 脚本：`download_wikipedia_raw_corpus.bash`

## 提取内容
   * 输入：`raw_data/zhwiki-latest-pages-articles.xml.bz2`
   * 输出：`extracted_json_data/**/*`
   * 脚本：`extract_wikipedia_json_corpus.bash`

## 转换成纯文本
   * 输入：`extracted_json_data/**/*`
   * 输出：`spacy_standard_plain_files/*`
   * 脚本：`json_corpus_to_plain_text.bash`

## 繁体中文转换成简体中文
   * 输入：`spacy_standard_plain_files/*`
   * 输出：`normaled_plain_files/*`
   * 脚本：`normal_text.bash`

## 分句并清理空行
   * 输入：`normaled_plain_files/*`
   * 输出：`sentence_data/*`
   * 脚本：`split_text_to_sentence.bash`

## 分词
   * 输入：`sentence_data/*`
   * 输出：`token_cleaned_plain_files/*`
   * 脚本：`token_plain_text.bash`
