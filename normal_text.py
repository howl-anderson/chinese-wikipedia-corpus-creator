#!/bin/env python

import sys
import pathlib

import opencc
import batch_executor_v2

converter = opencc.OpenCC("t2s.json")


def process_file(args):
    input_file, output_file = args

    with input_file.open("r") as input_fd, output_file.open("wt") as output_fd:
        content = input_fd.read()
        converted_content = converter.convert(content)
        output_fd.write(converted_content)


if __name__ == "__main__":
    input_dir = pathlib.Path(sys.argv[1])
    output_dir = pathlib.Path(sys.argv[2])

    batch_executor_v2.batch_executor_v2(input_dir, output_dir, process_file)
