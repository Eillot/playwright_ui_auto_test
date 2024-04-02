#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 14:41
# @Description : 【某某系统项目】-【登录】-界面自动化测试用例
# @Author  : Simon
# @File    : CaseForDigitalizedLogin.py
# @Software: IntelliJ IDEA

import allure
import time
import logging
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
from src.config.constant.env_url import TEST_ENV
from src.utils.FilesUtils import get_current_files_dir, current_files_add_list

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

save_videos_path = get_current_files_dir("../") + "\\videos"
load_target_webm = current_files_add_list(save_videos_path)


class CaseForDigitalizedLogin():
    @allure.description("""【某某系统项目】-【登录】-【界面自动化测试用例】""")
    def test_example(self):
        logger.info("【某某系统项目】-【登录】-【界面自动化测试用例】-【开始执行】")
        with sync_playwright() as p:
            browser_type = p.chromium
            browser = browser_type.launch(headless=False,slow_mo=6000)
            context = browser.new_context(
                record_video_dir=save_videos_path,
                record_video_size={"width": 640, "height": 480}

            )
            page = context.new_page()
            page.goto(TEST_ENV)
            time.sleep(6)
            page.get_by_role("textbox", name="请输入账号").click()
            page.locator("#username").fill("user_name")
            page.get_by_role("textbox", name="请输入密码").click()
            page.locator("#password").fill("pass_word")
            page.get_by_role("button", name="登录").click()
            time.sleep(2)
            """断言"""
            expect(page).to_have_title("页面标题名称")
            logger.info("【某某系统项目】-【登录】-【界面自动化测试用例】-【结束执行】")
            context.close()
            browser.close()
            time.sleep(10)
            allure.attach.file(load_target_webm[len(load_target_webm) - 1],
                               name="【某某系统项目】-【页面】录制回放测试报告",
                               attachment_type=allure.attachment_type.MP4, extension="mp4")
