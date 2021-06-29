#!/bin/env python

import sys
import pathlib
from unittest import mock
from typing import Union

import thulac

import batch_executor_v2

with mock.patch("builtins.print") as _:  # disable print for now
    thu_tokenizer = thulac.thulac(seg_only=True)


def process_file(args: Union[pathlib.Path, pathlib.Path]):
    input_file, output_file = args

    # with THULAC
    with mock.patch("builtins.print") as _:  # disable print for now
        thu_tokenizer.cut_f(str(input_file.absolute()), str(output_file.absolute()))


if __name__ == "__main__":
    input_path = pathlib.Path(sys.argv[1])
    output_path = pathlib.Path(sys.argv[2])

    batch_executor_v2.batch_executor_v2(input_path, output_path, process_file)
