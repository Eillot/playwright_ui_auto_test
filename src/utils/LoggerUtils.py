#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/1/24 15:00
# @Description :
# @Author  : Simon
# @File    : LoggerUtils.py
# @Software: IntelliJ IDEA

import logging

"""生成指定格式的日志"""
def generate_logger():
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    return logger
