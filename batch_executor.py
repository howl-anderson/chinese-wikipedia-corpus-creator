import os
import logging
from pathlib import Path

import joblib


def batch_executor(input_dir, output_dir, executor_object, n_jobs=-2):
    input_path = Path(input_dir)
    input_file_list = input_path.glob("**/*")

    output_path = Path(output_dir)

    executor_input_list = []

    for input_file_path in input_file_list:
        input_file_relative_name = input_file_path.relative_to(input_path)
        output_file_path = output_path / input_file_relative_name

        executor_input_list.append(
            (input_file_path.absolute(), output_file_path.absolute())
        )

    joblib.Parallel(n_jobs=n_jobs)(joblib.delayed(executor_object)(*i) for i in executor_input_list)
