import subprocess
import tempfile
import shutil
import os

with tempfile.TemporaryDirectory() as temp_dir:
    subprocess.call(
        "git clone https://github.com/howl-anderson/WikiExtractor.git {}".format(
            temp_dir
        ),
        shell=True,
    )

    shutil.copyfile(os.path.join(temp_dir, "WikiExtractor.py"), "./WikiExtractor.py")
