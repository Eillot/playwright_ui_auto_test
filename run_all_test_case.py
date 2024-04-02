#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/28 14:52
# @Author  : Simon
# @File    : run_all_test_case.py
# @Software: IntelliJ IDEA


import pytest
import os
from src.utils.FilesUtils import get_current_files_dir

"""批量执行PlaywRight框架录制的界面自动化测试Case"""
all_cases_path = get_current_files_dir("./ui_auto_test/src/case")

if __name__ == '__main__':
    pytest.main(['-s', '-q','./', '--clean-alluredir', '--alluredir=allure-results'])
    os.system('cp environment.properties ./allure-results/environment.properties')
    os.system("allure generate -c -o allure-report")