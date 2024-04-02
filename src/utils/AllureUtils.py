#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/1/24 15:38
# @Description :
# @Author  : Simon
# @File    : AllureUtils.py
# @Software: IntelliJ IDEA

import allure

"""基于自动化框架Allure封装,用于生成基于视频的测试报告"""
def create_allure_video_test_report(mp4_video_path,test_report_title):
    """
    :param mp4_video_path:已录制完毕视频保存路径
    :param test_report_title:测试报告标题
    :return:
    """

    allure.attach.file(source=mp4_video_path,name=test_report_title,
                       attachment_type=allure.attachment_type.MP4, extension="mp4")