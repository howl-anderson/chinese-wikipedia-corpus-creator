import logging
import re
import sys
import io
import pathlib

import batch_executor_v2

logger = logging.getLogger(__name__)


def split_text_to_sentence(args):
    input_file, output_file = args

    sentence_delimiter = ("。", "？", "?", "！", "!", "；", ";")

    output_lines = []
    with input_file.open("rt") as fd:
        for line in fd.readlines():
            # 在句子分割字符后追加换行符,以实现分割句子
            for delimiter in sentence_delimiter:
                line = re.sub(re.escape(delimiter), r"\g<0>\n", line)

            new_line_string = io.StringIO(line)

            for line_text in new_line_string.readlines():
                # 清理头尾的换行符以及其他不可见字符
                line_text = re.sub(r"^\s+", "", line_text)
                line_text = re.sub(r"\s+$", "", line_text)

                logger.debug(line_text)

                if not line_text:  # empty string is skiped
                    continue

                output_lines.append(line_text)

    with output_file.open("wt") as fd:
        fd.writelines((i + "\n" for i in output_lines))


if __name__ == "__main__":
    input_dir = pathlib.Path(sys.argv[1])
    output_dir = pathlib.Path(sys.argv[2])

    batch_executor_v2.batch_executor_v2(input_dir, output_dir, split_text_to_sentence)
