#!/bin/env python

import sys
import pathlib
import json
import os

from joblib import Parallel, delayed
from tqdm import tqdm
from bs4 import BeautifulSoup
import batch_executor_v2


def process_file(args):
    input_file, output_dir = args

    with input_file.open("rt") as input_fd:
        soup = BeautifulSoup(input_fd.read(), "html.parser")
        for index, line in enumerate(soup.find_all("doc")):
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / str(index)

            plain_data = line.text

            with output_file.open("wt") as output_fd:
                output_fd.write(plain_data)


if __name__ == "__main__":
    input_dir = pathlib.Path(sys.argv[1])
    output_dir = pathlib.Path(sys.argv[2])

    batch_executor_v2.batch_executor_v2(input_dir, output_dir, process_file)
