[README written in English](README.md)
------------------------------

# 中文 Wikipedia 维基百科语料库构建工具

本项目提供了工作流和脚本工具，从零开始创建中文维基百科语料库。

## 开始使用

克隆或者下载本repo志本地文件系统

### 系统要求&软件依赖

支持 python 3.4+, 不支持 python2

#### Ubuntu/debian 用户

脚本 `install_dependencies_on_ubunut.bash` 会帮你自动安装好所有的依赖

#### 其他操作系统用户
##### python 软件包

使用如下命令安装所需的 python 依赖：

```bash
pip install -r ./requirements.txt
```

##### 非 python 软件包

需要安装 [OpenCCC](https://github.com/BYVoid/OpenCC)，用户按照官方的指示，安装即可。

Uubntu / debian 用户，使用 `apt` 命令即可：

```bash
sudo apt-get install opencc
```



### 使用

#### 全自动脚本

`allinone_process.bash`

#### 手动运行

见 [workflow](workflow.zh-Hans.md)
