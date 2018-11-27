from pathlib import Path
from tqdm import tqdm


def read_lines_from_input(input_files):
    for fname in tqdm(input_files):
        with open(fname) as infile:
            yield [i.strip() for i in infile]


def split(input_files, file_path_prefix,
          file_name_suffix='',
          append_trailing_newlines=True,
          mini_line_length=100000):
    shard_id = -1
    input_iterator = read_lines_from_input(input_files)

    while True:
        line_counter = 0
        line_buffer = []
        shard_id += 1

        output_file_name = '{}-{}{}'.format(file_path_prefix, shard_id,
                                            file_name_suffix)
        with open(output_file_name, 'wt') as outfile:
            try:
                while True:
                    file_lines = next(input_iterator)
                    line_counter += len(file_lines)
                    line_buffer.extend(file_lines)

                    if line_counter >= mini_line_length:
                        outfile.write('\n'.join(line_buffer))

                        if append_trailing_newlines:
                            outfile.write('\n')

                        break
            except StopIteration:
                if line_buffer:
                    outfile.write('\n'.join(line_buffer))
                    if append_trailing_newlines:
                        outfile.write('\n')
                break


if __name__ == "__main__":
    input_files = [str(i.absolute()) for i in Path('token_cleaned_plain_files').glob('*wiki*') if i.is_file()]

    split(input_files, './sharded_files/data.txt')
