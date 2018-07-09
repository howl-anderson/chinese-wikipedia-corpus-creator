[中文版本的 README](README.md)
------------------------------

# Chinese Wikipedia corpus creater

Workflow and scripts that help user create Chinese Wikepedia corpus easily form scratch.

## Getting Started

Clone or download this repo to local filesystem.

### Prerequisites

Python 3.4+ is well supported, python2 is not supported.

#### For ubuntu/debian user

Script `install_dependencies_on_ubunut.bash` will install everything for you.

#### For other operation system user

##### python packages
install requirements by:

```bash
pip install -r ./requirements.txt
```

##### non-python packages

[OpenCCC](https://github.com/BYVoid/OpenCC) is required. User should install it by self.

For Uubntu / debian user, `opencc` can be installed by command `apt`：

```bash
sudo apt-get install opencc
```

### Usage
#### All in one script

`allinone_process.bash`

#### Manual running

see [workflow](workflow.md)

## TODO

Jieba has a poor model performance, replace it with [LTP](https://github.com/HIT-SCIR/ltp) or [THULAC](https://github.com/thunlp/THULAC), prefer using `THULAC` for it's an open source software.
