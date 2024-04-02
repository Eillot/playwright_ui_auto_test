#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2023/12/28 14:56
# @Author  : Simon
# @File    : FilesUtils.py
# @Software: IntelliJ IDEA

import os
import glob

"""获取当前文件路径"""
def get_current_files_dir(current_dir='./'):
    current_file_name = os.path.dirname(os.path.abspath(current_dir))
    return current_file_name


"""将指定目录下的所有文件以list的形式加载并展示"""
def current_files_add_list(target_dirname):
    files_list = glob.glob(target_dirname)
    return files_list
