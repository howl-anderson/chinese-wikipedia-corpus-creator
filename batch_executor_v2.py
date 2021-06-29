import os
import logging
import multiprocessing
from pathlib import Path

import tqdm

from typing import Callable


def batch_executor_v2(input_dir: Path, output_dir: Path, executor_object: Callable):
    input_path = input_dir
    input_file_list = input_path.rglob("*")
    # filter out hidden files (e.g. .gitignore)
    input_file_list = filter(
        lambda x: x.is_file() and not x.parts[-1].startswith("."), input_file_list
    )

    output_path = output_dir

    executor_input_list = []

    for input_file_path in input_file_list:
        output_file_path = output_path / input_file_path.relative_to(input_path)
        # make sure parent dir exists
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        executor_input_list.append((input_file_path, output_file_path))

    with multiprocessing.Pool() as pool:
        results = []
        for r in tqdm.tqdm(pool.imap_unordered(executor_object, executor_input_list)):
            results.append(r)

    return results
