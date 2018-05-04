#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import


import sys
import pathlib

import jieba
import joblib
from tqdm import tqdm

input_dir = sys.argv[1]
input_path = pathlib.Path(input_dir)
input_files = input_path.glob("**/*")

# filter out hidden files (e.g. .gitignore)
input_files = filter(lambda x: not x.parts[-1].startswith('.'), input_files)

output_dir = sys.argv[2]
output_path = pathlib.Path(output_dir)


def process_file(input_file_path):
    input_file = str(input_file_path.absolute())
    output_file_path = output_path / input_file_path.parts[-1]
    output_file = str(output_file_path.absolute())
    with open(input_file, 'rt') as in_fd, open(output_file, 'wt') as out_fd:
        output_lines = []
        for line in in_fd:
            seg_list = jieba.cut(line, cut_all=False)
            output_line = " ".join(filter(lambda x: x != " ", seg_list))   # 精确模式

            output_lines.append(output_line)

        out_fd.writelines(output_lines)

        
joblib.Parallel(n_jobs=-2)(joblib.delayed(process_file)(input_file) for input_file in tqdm(input_files))
