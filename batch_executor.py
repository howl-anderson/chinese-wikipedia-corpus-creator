import os
import logging
import multiprocessing
from pathlib import Path

import tqdm


def batch_executor(input_dir, output_dir, executor_object, n_jobs=-1):
    input_path = Path(input_dir)
    input_file_list = input_path.glob("**/*")

    # filter out hidden files (e.g. .gitignore)
    input_file_list = filter(
        lambda x: x.is_file() and not x.parts[-1].startswith("."), input_file_list
    )

    output_path = Path(output_dir)

    executor_input_list = []

    for input_file_path in input_file_list:
        input_file_relative_name = input_file_path.relative_to(input_path)
        output_file_path = output_path / input_file_relative_name

        executor_input_list.append(
            (str(input_file_path.absolute()), str(output_file_path.absolute()))
        )

    # with joblib
    # import joblib
    # joblib.Parallel(n_jobs=n_jobs)(
    #     joblib.delayed(executor_object)(*i) for i in tqdm(executor_input_list)
    # )

    # with multiprocessing
    with multiprocessing.Pool() as pool:
        results = []
        for r in tqdm.tqdm(pool.imap_unordered(executor_object, executor_input_list)):
            results.append(r)

    return results
