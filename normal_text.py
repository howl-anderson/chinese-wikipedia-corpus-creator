#!/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import


import sys
import pathlib
import subprocess

import joblib
from tqdm import tqdm

input_dir = sys.argv[1]
input_path = pathlib.Path(input_dir)
input_files = input_path.glob("**/*")

output_dir = sys.argv[2]
output_path = pathlib.Path(output_dir)


def process_file(input_file_path):
    input_file = str(input_file_path.absolute())
    output_file_path = output_path / input_file_path.parts[-1]
    output_file = str(output_file_path.absolute())

    cmd = ['opencc', '-i', input_file, '-o', output_file, '-c', 'zht2zhs.ini']

    cmd_string = " ".join(cmd)
    
    subprocess.call(cmd_string, shell=True)
        
joblib.Parallel(n_jobs=-2)(joblib.delayed(process_file)(input_file) for input_file in tqdm(input_files))
