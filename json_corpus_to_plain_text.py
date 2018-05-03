#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import sys
import pathlib
import json
import os

from joblib import Parallel, delayed
from tqdm import tqdm


input_dir = sys.argv[1]
output_dir = sys.argv[2]

input_path = pathlib.Path(input_dir)

input_files = input_path.glob("**/wiki_*")


def process_file(input_file):
    input_file_relative_name = input_file.relative_to(input_dir)
    output_file_name = "-".join(input_file_relative_name.parts)

    with input_file.open('rt') as input_fd:
        for index, line in enumerate(input_fd):
            data_obj = json.loads(line)

            output_file = os.path.join(output_dir, output_file_name + "_" + str(index))
            output_path = pathlib.Path(output_file)

            plain_data = data_obj['text']

            with output_path.open('wt') as output_fd:
                output_fd.write(plain_data)


Parallel(n_jobs=-2)(delayed(process_file)(input_file) for input_file in tqdm(input_files))
