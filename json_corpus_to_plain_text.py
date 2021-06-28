#!/bin/env python

import sys
import pathlib
import json
import os

from joblib import Parallel, delayed
from tqdm import tqdm
from bs4 import BeautifulSoup


input_dir = sys.argv[1]
output_dir = sys.argv[2]

input_path = pathlib.Path(input_dir)

input_files = input_path.glob("**/wiki_*")


def process_file(input_file):
    input_file_relative_name = input_file.relative_to(input_dir)
    output_file_dir = output_dir / input_file_relative_name
    output_file_dir.mkdir(parents=True, exist_ok=True)

    with input_file.open("rt") as input_fd:
        soup = BeautifulSoup(input_fd.read(), 'html.parser')
        for index, line in enumerate(soup.find_all('doc')):
            output_file = output_file_dir / str(index)

            plain_data = line.text

            with output_file.open("wt") as output_fd:
                output_fd.write(plain_data)


Parallel(n_jobs=-1)(
    delayed(process_file)(input_file) for input_file in tqdm(input_files)
)
