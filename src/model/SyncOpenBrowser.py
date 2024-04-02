#!/usr/bin/env python
# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright


# @Time    : 2023/12/28 15:10
# @Author  : Simon
# @File    : SyncOpenBrowser.py
# @Software: IntelliJ IDEA

"""
基于playwright使用chrome浏览器网页并录制视频
"""
def playwright_open_brower(videos_save_path):
    with sync_playwright() as p:
        browser_type = p.chromium
        browser = browser_type.launch(headless=False)
        context = browser.new_context(
            record_video_dir=videos_save_path,
            record_video_size={"width": 640, "height": 480}

        )

